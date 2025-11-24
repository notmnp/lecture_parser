# week05

# Exam Study Notes – Computer Systems & RTOS Basics  

> **Key idea**: Think of the processor like a busy office.  
> - **Interrupts** are phone calls that can pause current work.  
> - **Exception handlers** are the voicemail that answers the call.  
> - **System calls** are formal requests to the office manager.  
> - **Schedulers** are the shift‑manager deciding who works next.  

--------------------------------------------------------------------

## Interrupts & IRQs  
- **Interrupt** – external signal to the CPU that a peripheral needs service.  
- **IRQ line** – each I/O device has its own line.  
- **Types**  
  - *External (hardware)* – e.g., a button press.  
  - *Internal fault* – e.g., memory page fault.  
  - *Trap (software)* – e.g., ARM’s `SVC` (Supervisor Call).  
- **Flow** –  
  1. Peripheral asserts its IRQ.  
  2. CPU saves context (registers + PC).  
  3. CPU jumps to ISR (Interrupt Service Routine).  
  4. ISR finishes, restores context, returns to main flow.

--------------------------------------------------------------------

## Exception Handling (Cortex‑M4)  
- **Vector Table** – array of addresses indexed by *vector number*.  
  - `vector[0]` → initial stack pointer value.  
  - `vector[1]` → `Reset_Handler`.  
  - `vector[38]` → `USART2_IRQHandler` (serial).  
  - `vector[40]` → `EXTI15_10_IRQHandler` (push button).  
  - `vector[15]` → `SysTick_Handler` / `PendSV_Handler`.  
- **Location** – placed at a fixed low‑memory address; the CPU loads the table on reset.  
- **Lookup process** –  
  1. Identify vector number.  
  2. Read address from table.  
  3. Push current context on stack.  
  4. Jump to handler.  
  5. Handler returns → pop context.

--------------------------------------------------------------------

## Nested Interrupts & Priorities  
- Each IRQ has a numeric **priority** (lower number → higher priority).  
- **Preemption rule** – a higher‑priority IRQ can interrupt a running lower‑priority ISR.  
- **Example** –  
  ```
  app code → IRQ0 (low) → ISR0
                ↘  IRQ1 (high) → ISR1
                        (ISR1 completes) → resume ISR0 → resume app
  ```  
- **Analogy** – an urgent phone call can interrupt a less urgent one in the middle of a conversation.

--------------------------------------------------------------------

## System Calls & Execution Modes  
| Mode | Typical user | Permissions | Typical handler |
|------|--------------|-------------|-----------------|
| **Thread** | Application code | Unprivileged | Runs in **Unprivileged** mode |
| **Handler** | ISR / OS kernel | Privileged | Runs in **Privileged** mode |

- **SVC (Supervisor Call)** – software instruction that triggers a privileged handler.  
- **Trap flow** –  
  1. App issues `SVC`.  
  2. CPU switches to Handler mode.  
  3. OS reads parameters, performs service.  
  4. Return to previous mode, resume app.

--------------------------------------------------------------------

## Bare‑Metal Scheduling (Super‑Loop)  
- No OS → a simple infinite loop.  
- **Typical pattern**  
  ```c
  while (1) {
      t1();  // e.g., sensor read
      t2();  // e.g., data process
      t3();  // e.g., transmit
  }
  ```
- **Execution frequency relation**  
  ```
  f_t1 = (3/2) * f_t2 = 3 * f_t3
  ```
- **Limitation** – slow response to asynchronous events (button press → delay equals sum of t2+t3+t2).

--------------------------------------------------------------------

## Foreground / Background Model  
- **Background** – super‑loop (regular tasks).  
- **Foreground** – ISRs that preempt the loop.  
- **Example** – button press triggers ISR → sets flag → main loop checks flag to run `t1`.  
- **Drawback** – latency = time of all preceding background tasks.

--------------------------------------------------------------------

## Concurrent Execution & Gantt View  
- **Concurrent** – multiple tasks interleaved on one or more CPUs.  
- **Round‑robin** – each task gets a timeslice; scheduler preempts at slice end.  
- **Gantt chart** – shows ready/run states, context switches.  
- **Real‑time task** – infinite loop with:
  - **Block** – wait for event (I/O, timer, sync).  
  - **Unblock** – becomes ready.  
- **Memory** – all tasks share code/data/heap; each has its own stack & TCB.

--------------------------------------------------------------------

## Task Control Block (TCB) – RTOS  
| Field | Meaning |
|-------|---------|
| `SP` | Current stack pointer |
| `StackSize` | Size of task stack |
| `Entry` | Function pointer to start address |
| `Priority` | Current priority (can change) |
| `BasePriority` | Original priority |
| `DelayUntil` | Timestamp when task will unblock |
| `Prev`, `Next` | Doubly‑linked list links (ready queue) |
| `State` | `{new, ready, running, blocked, terminated}` |

--------------------------------------------------------------------

## Context Switching (PendSV)  
1. **Save** current task’s registers onto its stack.  
2. **Store** current `SP` into current TCB.  
3. **Load** `SP` from next task’s TCB.  
4. **Restore** next task’s registers from its stack.  
5. Return to next task (normal execution resumes).  

- **PendSV** is a low‑priority exception used exclusively for context switches.

--------------------------------------------------------------------

## Task States & Scheduler Triggers  
| State | Transition | Trigger |
|-------|------------|---------|
| **New** | → Ready | Task creation |
| **Ready** | → Running | Scheduler picks it |
| **Running** | → Ready | Preempted or timeslice expires |
| **Running** | → Blocked | Wait for event |
| **Running** | → Terminated | Completed or killed |
| **Blocked** | → Ready | Event occurs |

- Scheduler runs on any of these triggers.

--------------------------------------------------------------------

## Real‑Time Scheduling Parameters  
- **T (Period)** – interval between successive releases.  
- **C (WCET)** – Worst‑Case Execution Time per period.  
- **D (Deadline)** – time by which the task must finish after release.  

Typical task loop:  
```c
while (1) {
    block();   // wait for event
    // critical section
}
```

--------------------------------------------------------------------

### Quick Reference Formulae  

| Concept | Formula / Value |
|---------|-----------------|
| Push‑button ISR vector | `vector[40] = EXTI15_10_IRQHandler` |
| Frequency relation | `f_t1 = 1.5·f_t2 = 3·f_t3` |
| Context switch cost | O(1) register pushes/pops |

--------------------------------------------------------------------

> **Remember**: Think of the CPU as a receptionist who must answer calls (interrupts), forward tasks to specialized workers (ISRs), and keep a to‑do list (TCB). The OS scheduler is the shift manager deciding who works next, while real‑time parameters are the contract deadlines the workers must meet.
