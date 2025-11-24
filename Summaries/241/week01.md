# week01

# Embedded Systems & C Programming – Quick‑Study Guide

## 1. Embedded Systems  
- **What is it?** A computer built into a larger device to perform a specific task.  
- **Real‑time requirement** – must finish events within a deadline.  
  - *Soft* deadlines: missing a few still works (e.g. video streaming).  
  - *Hard* deadlines: missing any is catastrophic (e.g. anti‑lock brakes).  
- **Typical components**  
  - **Sensors**: read the world (lidar, camera, switches).  
  - **Actuators**: drive the world (motors, servos, speakers).

> *Analogy*: Think of an embedded system as a tiny brain that must think and act fast enough to keep a car safe or a microwave on time.

## 2. Operating System vs Real‑Time OS (RTOS)  
| Feature | OS | RTOS |
|---------|----|------|
| Scheduler | Usually round‑robin or priority‑based but *non‑deterministic* | Deterministic (often fixed priority, priority‑inheritance). |
| Deadline guarantees | None | Guarantees that tasks meet their deadlines. |
| Response time | Variable, depends on load | Predictable, often measured in clock cycles. |
| Temporal correctness | Not a priority | As important as logical correctness. |

> *Analogy*: An OS is like a city where many drivers (processes) share the road; an RTOS is a traffic‑controlled intersection that always lets the right‑of‑way drivers through on schedule.

## 3. Why C Rules the Embedded World  
- **No garbage collector** – deterministic memory usage.  
- **Pointers** – direct access to memory‑mapped I/O.  
- **Small runtime library** – less code, less memory.  
- **Compiled** – runs at full speed.  

### C vs C++ (subset rule)  
- C is *strict*: no classes, no methods, no overloading, no exceptions.  
- All data is public, everything passes by value.  

> *Analogy*: C is like a Swiss Army knife – minimalistic but powerful; C++ adds extra tools that you may not need in a tiny embedded system.

## 4. Fixed‑Width Integer Types  
Use `#include <stdint.h>` to get predictable sizes.  
| Signed | Unsigned | Size |
|--------|----------|------|
| `int8_t` | `uint8_t` | 8 bits |
| `int16_t` | `uint16_t` | 16 bits |
| `int32_t` | `uint32_t` | 32 bits |
| `int64_t` | `uint64_t` | 64 bits |

> *Why?* Standard `int`/`short` etc. vary by compiler; using fixed‑width types ensures code behaves the same on every target.

## 5. Structs & Memory Layout  
```c
#include <stdint.h>

struct pair {          // two fields
    uint8_t  first;    // 1 byte
    uint32_t second;   // 4 bytes
};
```
- `sizeof(struct pair)` → **8 bytes** (1 + 3 padding + 4).  
- `sizeof(first)` → 1, `sizeof(second)` → 4.  

### Padding & Alignment  
- Compilers add padding so each field starts at an address that’s a multiple of its size (natural alignment).  
- Unaligned accesses are slower and may fault on some CPUs.  

> *Analogy*: Think of packing a suitcase: you add a bit of extra space (padding) so that each item (field) sits neatly and can be quickly found.

## 6. `typedef` to Simplify Structs  
```c
typedef struct {
    uint8_t  first;
    uint32_t second;
} pair_t;
```
- Now you can declare `pair_t p = {1, 2};` instead of `struct pair p`.  

## 7. Quick Reference – Size & Padding  
| Field | Size | Alignment | Offset | Padding |
|-------|------|-----------|--------|---------|
| `first`  | 1 | 1 | 0 | 0 |
| *Padding* | 3 | – | 1 | 3 |
| `second` | 4 | 4 | 4 | – |
| **Total** | 8 | – | – | – |

---

### Take‑away Cheat Sheet

- **Embedded** = a dedicated brain inside a device → real‑time → soft vs hard deadlines.  
- **RTOS** = deterministic scheduler → guaranteed timing.  
- **C** = low‑level, fast, predictable → no GC, pointers, small runtime.  
- **Fixed‑width types** = portability.  
- **Structs** = grouping data → watch alignment & padding.  
- **`typedef`** = cleaner type names.

Use this sheet to quickly recall the essentials before an exam or when writing code for an embedded project. Happy hacking!
