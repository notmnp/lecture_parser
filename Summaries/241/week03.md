# week03

# Computer Memory Cheat Sheet

## 1. Memory Types  

| Volatile | Non‑volatile | Typical use | Access time (approx.) |
|----------|--------------|-------------|------------------------|
| **SRAM** | **ROM** | Caches, startup code | 2 ns |
| **DRAM** | **Flash** | Main RAM, SSD storage | 25 ns |

* **Volatile** – data disappears when power is lost.  
* **Non‑volatile** – data stays after power off.  
* SRAM is **fast** but **expensive** (large silicon area).  
* DRAM is **cheap** but requires refresh.

---

## 2. Hard Disk Drive (HDD)  

```
         arm
          |
   ────────┬─────────────  platter (magnetic)
          │   head
          └─ spindle (rotates at 5400–7200 RPM)
```

* **Access time**  
  `T_access = T_seek + T_rotational`  

  *Seek* – moving the arm to the correct track.  
  *Rotational latency* – time for the right sector to spin under the head.  

  ```
  T_rotational ≈ 60 / (2 * RPM)   seconds
  ```
* Typical values  
  * Latency ≈ 5 ms  
  * Bandwidth ≈ 100 MiB/s  
  * Capacity ≈ TB

---

## 3. Solid State Drive (SSD) – Flash Memory  

* **Erase block**: ~128 KiB or larger.  
* **Program page**: ~4 KiB.  
* **Flash Translation Layer (FTL)** maps logical sectors → physical pages.  
* **Write Amplification** – to change a page, copy old data to a new page, old becomes invalid.  

### Lifetime Management  
| Technique | Purpose |
|-----------|---------|
| Wear‑leveling | Distribute erase cycles evenly across blocks. |
| Over‑provisioning | Reserve extra space for bad blocks and garbage‑collection. |

### Performance vs HDD  
* Latency ≈ 100× lower.  
* Bandwidth ≈ 5× higher.

---

## 4. Memory Organization & Endianness  

| Order | Example 0x1234ABCD |
|-------|---------------------|
| **Little‑Endian** | CD AB 34 12 (LSB at lowest address) |
| **Big‑Endian** | 12 34 AB CD (MSB at lowest address) |

* Most modern CPUs use little‑endian; network protocols often use big‑endian.  

---

## 5. Size Prefixes (SI vs IEC)  

| Prefix | Value | Prefix | Value |
|--------|-------|--------|-------|
| **k** (kilo) | 10³ | **Ki** (kibi) | 2¹⁰ = 1 024 |
| **M** (mega) | 10⁶ | **Mi** (mebi) | 2²⁰ |
| **G** (giga) | 10⁹ | **Gi** (gibi) | 2³⁰ |
| **T** (tera) | 10¹² | **Ti** (tebi) | 2⁴⁰ |
| **P** (peta) | 10¹⁵ | **Pi** (pebi) | 2⁵⁰ |
| **E** (exa) | 10¹⁸ | **Ei** (exbi) | 2⁶⁰ |

* **Memory** is usually counted in powers of 2 (KiB, MiB).  
* **Disk drives** advertise sizes in powers of 10 (TB = 10¹² bytes).

---

## 6. Memory Hierarchy  

| Level | Typical Size | Speed | Cost/Bit | Example |
|-------|--------------|-------|----------|---------|
| Registers | < 1 kB | 0 ns | Highest | CPU registers |
| L1 Cache | 32–64 KiB | ~10 ns | High | Split I/D cache |
| L2 Cache | 1–2 MiB | ~20 ns | Medium | Unified |
| L3 Cache | 2–9 MiB/core | ~50 ns | Lower | Shared between cores |
| Main Memory (DRAM) | 1–32 GiB | 25 ns | Low | System RAM |
| Secondary Storage (HDD/SSD) | 100 GiB–10 TiB | ~5 ms (HDD) | Very low | Hard drives |

**Rule of thumb:** *Speed ↓, Capacity ↑, Cost/Bit ↓.*

---

## 7. Cache Basics  

```
Processor  →  Cache  →  Main Memory
```

* **Cache line** – a contiguous block of memory (e.g., 4 words).  
* **Block size** – size of a memory block transferred to cache (e.g., 32‑bit words).  
* **Hit** – requested data already in cache.  
* **Miss** – not in cache → fetch from main memory.  
* **Data fetched on demand** – only when the processor requests it.

---

## 8. Locality of Reference  

| Type | What it means | Example |
|------|----------------|---------|
| **Temporal** | Data used again soon | Loop counter in a `for` loop |
| **Spatial** | Adjacent data accessed soon | Elements of an array |

* Caches exploit both by loading whole blocks when one word is requested, increasing hit rate.

---

## 9. Dual‑Core Cache Architecture  

| Cache | Typical Size | Sharing | Notes |
|-------|--------------|---------|-------|
| **L1‑I** (Instruction) | 32–64 KiB | Private | Enables parallel fetch |
| **L1‑D** (Data) | 32–64 KiB | Private | Split from L1‑I |
| **L2** | 1–2 MiB | Private | Unified I/D |
| **L3** | 2–9 MiB/core | Shared | Largest shared cache |

---

## 10. Virtual Memory  

| Concept | Description |
|---------|-------------|
| **Virtual address space** | Each process sees a contiguous address space (0 → 0xFFFFFFFF on 32‑bit). |
| **Paging** | Fixed‑size pages (4–8 KiB). |
| **Page table** | Maps virtual pages → physical frames. |
| **Page fault** | When a page is not in RAM → OS loads it from disk into memory. |
| **Swapping** | Off‑loaded pages moved to secondary storage (HDD/SSD). |

**Benefits**  
1. Enlarges usable memory per process.  
2. Allows many processes to coexist (multitasking).  
3. Protects each process’s memory.  
4. Supports hibernation and over‑commitment.

---

### Quick Formulas  

* **Rotational latency (half rotation)**  
  `T_rot = 60 / (2 * RPM)  seconds`  

* **SI vs IEC**  
  `k = 10^3` vs `Ki = 2^10`  

---

> **Remember**:  
> * Memory is a trade‑off ladder – smaller levels are faster and more expensive; larger levels are slower and cheaper.  
> * Endianness decides how a multi‑byte value is laid out in memory.  
> * SSDs are essentially HDDs with flash chips; they get their performance from the speed of flash and clever wear‑leveling.  
> * Virtual memory turns a computer’s RAM into a big, protected, and flexible address space.
