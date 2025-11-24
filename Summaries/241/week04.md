# week04

# Exam Study Cheat‑Sheet

**Virtual ↔ Physical Address Translation**  
- **MMU**: hardware inside the CPU that turns a *virtual* address into a *physical* address.  
- **Page table**: a table indexed by the virtual page number (VPN). Each entry contains  
  - Physical page number (PPN)  
  - Valid bit (1 = in RAM, 0 = needs a page fault)  
  - Swap entry (if not valid).  
- **Formula**  
  ```text
  physical = (VPN * page_size) + offset
  ```
  *Analogy*: think of a library shelf (VPN) and the exact spot on that shelf (offset).*

**Memory‑Mapped I/O (MMIO)**  
- Devices expose registers at fixed memory addresses.  
- Reading/writing those addresses performs I/O.  
- Example (STM32F401):  
  | Address Range | Device   |
  |---------------|----------|
  | 0x2000 0000–0x2001 8000 | SRAM      |
  | 0x4001 2000–0x4001 2400 | ADC       |
  | 0x4001 3000–0x4001 3400 | SPI       |
  | 0x4002 0000–0x4003 0000 | GPIO      |
  | 0x8000 0000–0x8008 0000 | Flash     |

**GPIO Registers (per port)**  
| Register | Offset | Type | Purpose |
|----------|--------|------|---------|
| MODER | 0x00 | r/w | Pin mode (input, output, …) |
| OTYPER | 0x04 | r/w | Output type (push‑pull/open‑drain) |
| OSPEEDR | 0x08 | r/w | Output speed |
| PUPDR | 0x0C | r/w | Pull‑up / pull‑down |
| IDR | 0x10 | r/o | Input data |
| ODR | 0x14 | r/w | Output data |
| BSRR | 0x18 | w/o | Bit set/reset |
| LCKR | 0x1C | r/w | Lock configuration |
| AFRL | 0x20 | r/w | Alternate function low |
| AFRH | 0x24 | r/w | Alternate function high |

**Base address example**  
```c
#define GPIOA ((volatile GPIO_TypeDef *)0x40020000)
```
Access ODR: `GPIOA->ODR`.

**Bitwise tricks**  
- Set bit 5: `GPIOA->ODR |= (1U << 5);`  
- Clear bit 5: `GPIOA->ODR &= ~(1U << 5);`  
- Check bit 13 (push‑button low = pressed):  
  ```c
  if ((GPIOC->IDR & (1U << 13)) == 0)  // pressed
      ...
  ```

**Polling**  
- Repeatedly read a status register until a flag becomes set.  
- Simple but wastes CPU cycles.  
- Example (USART2 RXNE):  
  ```c
  while (!(USART2->SR & (1U << 5))) {}   // wait until RXNE
  uint8_t data = USART2->DR;             // read byte
  ```
- Efficiency estimate:  
  - 84 MHz CPU → loop ≈ 21 MHz  
  - 115200 baud → ~11520 B/s  
  - Loop iterations per byte ≈ 21 MHz / 11520 ≈ 1823 → *very high overhead*.

**Interrupts vs Polling**  
- **Polling**: CPU constantly asks, “Did this happen?”  
- **Interrupt**: Device signals the CPU (`IRQ`) when it needs service.  
  - CPU stops doing other work, jumps to interrupt handler.  
  - Efficient because CPU can sleep or do other tasks until needed.

**ARM Cortex‑M4 Basics**  
- 32‑bit word size, 4 GiB addressable space.  
- Little‑endian.  
- No cache.  
- Registers: R0–R12 (GP), R13 (SP), R14 (LR), R15 (PC).  
- Single‑precision FPU.  
- Pipelined – can retire 1 instruction per cycle.

**MCU Overview (STM32F401)**  
- Single chip: CPU, Flash (512 KiB), SRAM (96 KiB), peripherals.  
- Buses: AHB, APB1, APB2.  
- Key peripherals: GPIO, ADC, TIM, PWM, SPI, USART, USB.

---

*Use this sheet to recall the key definitions, equations, and example code snippets that underpin virtual memory, MMIO, GPIO programming, polling, serial communication, and interrupts on Cortex‑M4 microcontrollers.*
