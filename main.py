from tqdm import tqdm
import os
import sys
import glob
import shutil
import time
import base64
from openai import OpenAI
from pdf2image import convert_from_path
from dotenv import load_dotenv

# Constants
PDF_DIR = 'PDFs'
SUMMARY_DIR = 'Summaries'
TMP_IMG_DIR = 'tmp_slide_imgs'
useOLLAMA = False  # Set to True to use Ollama, False for Groq

# Model names and API endpoints
if useOLLAMA:
	OLLAMA_BASE_URL = 'http://localhost:11434/v1'
	VISION_MODEL = 'llava:7b'
	TEXT_MODEL = 'llama3:8b'
	API_BASE_URL = OLLAMA_BASE_URL
	API_KEY = 'ollama'  # Required by OpenAI client
else:
	VISION_MODEL = 'meta-llama/llama-4-scout-17b-16e-instruct'
	TEXT_MODEL = 'openai/gpt-oss-20b'
	API_BASE_URL = 'https://api.groq.com/openai/v1'
	API_KEY = None  # Will be loaded from .env
VISION_PROMPT = (
    "Provide a detailed, faithful summary of this lecture slide. "
    "Capture ALL content: equations, formulas, definitions, bullet points, and any written text. "
    "If the slide contains diagrams or images, describe what is shown (axes, shapes, arrows, labels, curves, intersections, etc.). "
    "Do not omit or simplify — include more detail rather than less, so no context is lost. "
    "This is not a final summary; it is a comprehensive capture of everything on the slide for later distillation."
)
TEXT_PROMPT = (
    "You are given detailed slide-by-slide summaries of a lecture. "
    "Rewrite them into *concise exam study notes* that are also easy to understand "
    "for someone not yet fully comfortable with the material. "
    "Important rules: "
    "- DO NOT mention slides, slide numbers, or page numbers. "
    "- DO NOT organize content by slide. "
    "- Keep only the essential equations, definitions, and canonical examples. "
    "- **Add short plain-language explanations or analogies to make the math intuitive.** "
    "- Eliminate all instructions, problem statements, and filler prose. "
    "- Do not repeat concepts. "
    "- Use clean bullet points with equations + concise explanations. "
    "- Think of it as a one-page cheat sheet that is both compact and understandable."
)
MAX_IMG_PIXELS = 33_000_000
MAX_IMG_SIZE_MB = 4

def load_api_key():
	load_dotenv()
	key = os.getenv('GROQ_API_KEY')
	if not key:
		print('GROQ_API_KEY not found in .env')
		sys.exit(1)
	return key

def ensure_dirs():
	os.makedirs(SUMMARY_DIR, exist_ok=True)
	os.makedirs(TMP_IMG_DIR, exist_ok=True)

def pdf_to_jpegs(pdf_path, out_dir):
	try:
		images = convert_from_path(pdf_path, fmt='jpeg')
	except Exception as e:
		print(f'Error converting {pdf_path} to images: {e}')
		return []
	img_paths = []
	for idx, img in enumerate(images):
		# Check size constraints
		w, h = img.size
		pixels = w * h
		if pixels > MAX_IMG_PIXELS:
			scale = (MAX_IMG_PIXELS / pixels) ** 0.5
			new_w, new_h = int(w * scale), int(h * scale)
			img = img.resize((new_w, new_h))
		img_path = os.path.join(out_dir, f'slide_{idx+1}.jpeg')
		img.save(img_path, 'JPEG')
		# Check file size
		if os.path.getsize(img_path) > MAX_IMG_SIZE_MB * 1024 * 1024:
			print(f'Slide {idx+1} in {pdf_path} exceeds {MAX_IMG_SIZE_MB}MB after resizing, skipping.')
			os.remove(img_path)
			continue
		img_paths.append(img_path)
	return img_paths

def call_groq_vision(client, img_path, retries=3):
	with open(img_path, 'rb') as f:
		img_bytes = f.read()
	img_b64 = base64.b64encode(img_bytes).decode()
	for attempt in range(retries):
		try:
			response = client.chat.completions.create(
				model=VISION_MODEL,
				messages=[{
					"role": "user",
					"content": [
						{"type": "text", "text": VISION_PROMPT},
						{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
					]
				}]
			)
			return response.choices[0].message.content.strip()
		except Exception as e:
			print(f'Vision API call failed: {e}')
			time.sleep(2)
	return '[Vision API failed]'

def call_groq_text(client, summary_block, retries=3):
	for attempt in range(retries):
		try:
			response = client.chat.completions.create(
				model=TEXT_MODEL,
				messages=[{
					"role": "user",
					"content": TEXT_PROMPT + "\n\n" + summary_block
				}]
			)
			return response.choices[0].message.content.strip()
		except Exception as e:
			print(f'Text API call failed: {e}')
			time.sleep(2)
	return '[Text API failed]'

def process_pdf(pdf_path, client):
	lecture_name = os.path.splitext(os.path.basename(pdf_path))[0]
	img_dir = TMP_IMG_DIR
	img_paths = pdf_to_jpegs(pdf_path, img_dir)
	if not img_paths:
		print(f'No valid slides found in {pdf_path}.')
		return
	slide_summaries = []
	total_steps = len(img_paths) + 1  # slides + final summary
	with tqdm(total=total_steps, desc=f"{lecture_name} (Slide Summarization)", unit="step") as pbar:
		for idx, img_path in enumerate(img_paths):
			pbar.set_description(f"{lecture_name} (Slide {idx+1} Summarization)")
			summary = call_groq_vision(client, img_path)
			slide_summaries.append(f'Slide {idx+1}: {summary}')
			pbar.set_postfix_str(f"Slide {idx+1}")
			pbar.update(1)
		# Aggregate summaries
		summary_block = '\n'.join(slide_summaries)
		pbar.set_description(f"{lecture_name} (Final Summary)")
		lecture_notes = call_groq_text(client, summary_block)
		pbar.set_postfix_str("Final summary")
		pbar.update(1)
	# Write output
	out_path = os.path.join(SUMMARY_DIR, f'{lecture_name}.md')
	with open(out_path, 'w') as f:
		f.write(f'# {lecture_name}\n\n')
		f.write(lecture_notes + '\n')
	print(f'  Output written to {out_path}')
	# Clean up images
	for img_path in img_paths:
		try:
			os.remove(img_path)
		except Exception as e:
			print(f'  Could not delete {img_path}: {e}')

def main():
	ensure_dirs()
	if useOLLAMA:
		client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
	else:
		api_key = load_api_key()
		client = OpenAI(base_url=API_BASE_URL, api_key=api_key)
	pdfs = glob.glob(os.path.join(PDF_DIR, '*.pdf'))
	if not pdfs:
		print('No PDF files found in PDFs/.')
		return
	for pdf_path in pdfs:
		process_pdf(pdf_path, client)
	# Clean up tmp dir
	try:
		shutil.rmtree(TMP_IMG_DIR)
	except Exception:
		pass

if __name__ == '__main__':
	main()
