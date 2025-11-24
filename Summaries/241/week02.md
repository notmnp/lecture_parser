# week02

# C Programming & Embedded Systems – Quick‑Reference Cheat Sheet  

---

## Dynamic Memory Allocation  
- **`malloc(size)`** – allocate `size` bytes → returns `void *`.  
- **`calloc(nmemb, size)`** – allocate `nmemb * size` bytes → zeroed memory.  
- **`realloc(ptr, size)`** – resize block `ptr` to `size`.  
- **`free(ptr)`** – deallocate; afterwards `ptr` is *dangling*.  
- **`void *`** is a *generic* pointer; implicit cast to any object pointer.  
- **Good practice** – after `free` set pointer to `NULL`.  

> *Analogy*: Think of `malloc` as renting a house (memory block), `free` as moving out, and `NULL` as saying “I’m not living anywhere right now.”

---

## Function Pointers  
- Define a type: `typedef int (*funcPtr_t)(int, int);`  
- Assign:  
  ```c
  funcPtr_t fp = sum;      // fp → address of sum()
  int r = fp(2,3);         // calls sum(2,3)
  fp = product;            // now points to product()
  ```
- **Uses**: callbacks, strategy patterns, dynamic dispatch.

> *Analogy*: A function pointer is a telephone number that you can change to call different people (functions) at the same time.

---

## C Strings  
- **Definition** – null‑terminated character array:  
  ```c
  char s[] = "abc";      // {'a','b','c','\0'}
  ```
- **Header** – `#include <string.h>`
- **Key functions**  
  - `strlen(const char *)` → length (excluding `'\0'`).  
  - `strcpy(char *, const char *)` → copy.  
  - `strcat(char *, const char *)` → concatenate.  
  - `strcmp(const char *, const char *)` → compare.  
- **Dynamic string**  
  ```c
  char *p = malloc(4);          // space for "abc" + '\0'
  strcpy(p, "abc");
  p = realloc(p, 10);           // grow, keep contents
  strcat(p, "def");
  ```
- **String literal** – stored in read‑only memory; modifying it is UB.  

> *Analogy*: A string is like a word in a book – it ends with a special end‑of‑word marker (`'\0'`).

---

## Preprocessor Basics  
- **Directives** start with `#`.  
- **Header inclusion**  
  ```c
  #include <stdio.h>   // system header
  #include "my.h"      // local header
  ```
- **Object‑like macro**  
  ```c
  #define BUFFER_SIZE 1024
  ```
- **Function‑like macro**  
  ```c
  #define MIN(a,b) ((a) < (b) ? (a) : (b))
  ```
- **Predeclared macros** – `__FILE__`, `__LINE__`, `__DATE__`, etc.  
  ```c
  printf("Error at %s:%d\n", __FILE__, __LINE__);
  ```

> *Analogy*: The preprocessor is a copy‑paste editor that runs before the compiler sees the code.

---

## Conditional Compilation & Include Guards  
- **`#ifdef / #else / #endif`** – include code only if a macro is defined.  
- **Include guard** (prevent double inclusion):  
  ```c
  #ifndef _STDIO_H_
  #define _STDIO_H_
  /* contents */
  #endif
  ```
- Alternative: `#pragma once`.

> *Analogy*: Think of include guards as a “do not open this box twice” label.

---

## C Memory Layout (Process)  
| Region | Order (high → low) | Contents |
|--------|-------------------|----------|
| **Stack** | top | local vars, function frames |
| **Heap** | middle | dynamic allocation |
| **Data** | below heap | global/static (initialized) |
| **Text** | bottom | machine instructions |

- **High address** → stack grows downwards.  
- **Low address** → text segment (code).  
- **Initialization**: globals = 0 if not specified; locals & heap uninitialized.

> *Analogy*: Stack = a pile of plates you keep adding to the top, heap = a toolbox you pull items from anywhere.

---

## STM32F401RE Memory Map  
| Segment | Address | Read/Write | Contents |
|---------|---------|------------|----------|
| **FLASH** | 0x0800 0000 | R/O | text, rodata, initialized data, BSS |
| **RAM**   | 0x2000 0000 | R/W | stack, heap, run‑time data |

- **Startup**: linker script `STM32F401RETX_FLASH.ld` places code in FLASH, data sections in RAM.  
- **During reset**: copy init values from FLASH to RAM, zero BSS.

> *Analogy*: FLASH is like a book stored on a shelf (read‑only), RAM is a desk where you work (writeable).

---

## Tool Chain Flow  
1. **Preprocessing** (`cpp`) – macro expansion, header inclusion.  
2. **Compilation** (`gcc`/`clang`) – generate assembly.  
3. **Assembling** (`gas`) – turn assembly into object files (`.o`).  
4. **Linking** (`ld`) – combine object files + libraries → ELF executable.  
5. **Loading** – program placed in memory as per linker script.  

- **Object files** contain machine code but cannot run alone.  
- **ELF** (Executable and Linkable Format) – standard binary format for embedded & Linux.

> *Analogy*: Think of the tool chain as a factory: raw code → assembly → product → packaging (ELF).

---

## STM32 Startup Sequence  
1. **Reset Handler** (`Reset_Handler`) – entry after power‑up or reset.  
2. **Initialize hardware** – e.g., enable FPU.  
3. **Copy data segment** – from FLASH to RAM.  
4. **Zero BSS** – clear uninitialized globals.  
5. **Call `main()`** – program’s entry point.  
6. **`main()` should never return** – usually ends with an infinite loop or reset.

> *Analogy*: The startup routine is like a robot’s boot‑up routine: power on → initialize parts → load program → start executing.

---

## Safety‑Critical Coding Rules (Gerard J. Holzmann)  
1. **Simple flow** – no `goto`, `setjmp/longjmp`, or recursion.  
2. **Fixed‑bound loops** – prevent runaway loops.  
3. **No dynamic memory after init** – deterministic behavior.  
4. **Small functions** – ≤ 60 lines (≈ 1 page).  
5. **Assertions** – ≥ 2 per function.  
6. **Minimal scope** – declare data as close to its use as possible.  
7. **Check return values** – every non‑void function call.  
8. **Limited preprocessor** – only headers & simple macros.  
9. **Simple pointers** – one level of dereference, no function pointers.  
10. **Compile with warnings** – pedantic settings, static analysis daily.

> *Analogy*: These rules are the safety protocols of a space mission – everything must be predictable and thoroughly checked.

---

## Computer System Architecture (High‑Level)  
- **Processor** – central unit, connected to peripherals via *system bus*.  
- **Peripherals**  
  - **GPU** – graphics processing.  
  - **Clock** – timing.  
  - **I/O** – input/output devices.  
- **Memory**  
  - **NVM** (e.g., flash) – stores startup code, non‑volatile data.  
  - **RAM** – runtime data & instructions.  
  - **Secondary storage** (HDD/SSD) – large capacity, slower access.  

> *Analogy*: The processor is the brain, the bus is the nervous system, peripherals are limbs and organs, NVM is the long‑term memory, RAM is the short‑term working memory, and HDD/SSD is the archive.

---
