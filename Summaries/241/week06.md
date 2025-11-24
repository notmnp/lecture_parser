# week06

# Real‑Time Scheduling Cheat Sheet

## 1.  Scheduling Objectives  
- **Meet all deadlines** (or keep lateness as low as possible).  
- **Maximize processor utilization**:  
  $$
  U=\sum_{i=1}^{n}\frac{C_i}{T_i}\quad\text{(busy fraction)}
  $$  
- **Minimize scheduler overhead** – keep the decision time small (ideally $O(1)$).  

*Analogy:* Think of a chef (processor) serving a set of dishes (tasks). The chef wants to finish every dish before its customer leaves (deadline), keep the kitchen busy, and not waste time ordering ingredients (overhead).

---

## 2.  Task Model  
- $\tau_i$: periodic task  
  - $C_i$: computation time (execution length)  
  - $T_i$: period (time between releases)  
  - $D_i$: relative deadline (often $D_i = T_i$)

---

## 3.  Non‑Preemptive Scheduling  
1. **Check utilization** – must be $\le 1$.  
2. **Schedule length** – Least Common Multiple of all periods.  
   *LCM* is the horizon where the pattern repeats.  
3. **Schedule construction** – use non‑preemptive EDF (schedule the ready task whose deadline is soonest).  

*Example:*  
$\tau_1:(C=8,T=18), \tau_2:(10,30), \tau_3:(10,45)$  
$U = 8/18 + 10/30 + 10/45 \approx 1$ – OK.  
Schedule length $= \operatorname{lcm}(18,30,45)=90$.

---

## 4.  Calculating LCM (prime‑factor method)  
1. Factor each period into primes.  
2. Take each prime with its highest exponent across all factorizations.  
3. Multiply them.  

*Example:*  
$18=2^1 3^2,\;30=2^1 3^1 5^1,\;45=3^2 5^1$ →  
$ \operatorname{lcm}=2^1 3^2 5^1 = 90$.

---

## 5.  Scheduling Policies

| Policy | Priority rule | Preemption | Typical use |
|--------|----------------|------------|-------------|
| **Rate‑Monotonic (RM)** | Shorter period → higher priority | **No** (fixed‑priority) | Classic real‑time tasks |
| **Earliest Deadline First (EDF)** | Earliest absolute deadline | **Yes** (dynamic priority) | Optimal for utilization up to 1 |
| **Fixed‑Priority Preemptive (FPP)** | Static priorities (compile‑time) | **Yes** | Simple to implement |
| **Round‑Robin (RR)** | Time‑slices, equal priority | Yes | Time‑sharing, not deadline‑aware |

---

## 6.  RM Utilization Bound  
For $n$ tasks, if  
$$
U=\sum_{i=1}^{n}\frac{C_i}{T_i} \le n\,(2^{1/n}-1)
$$  
then the task set is schedulable under RM.  
For large $n$, the bound approaches **0.69** (≈ 69 % utilization).

*Analogy:* The kitchen can only handle about 2/3 of the orders if every dish has a fixed preparation time.

---

## 7.  EDF Schedulability Test  
For any number of periodic tasks,  
$$
U=\sum_{i=1}^{n}\frac{C_i}{T_i}\le 1 \quad\Longrightarrow\quad \text{schedulable}
$$  
If utilization exceeds 1, no EDF schedule can meet all deadlines.  

*Example:*  
$\tau_1:(2,4), \tau_2:(3,10)$ → $U=2/4+3/10=0.8$ – OK.

---

## 8.  Fixed‑Priority Preemptive (FPP) Implementation  
- Maintain an **array of queues**, one per priority level.  
- The scheduler always picks the highest‑nonempty queue.  
- Enqueue/dequeue operations are $O(1)$.  

*Priority levels:* 0 (idle) to $P_{\max}$.  
*Example priorities:* Idle 0, τ1 2, τ2 2, τ3 5, …

---

## 9.  Round‑Robin Preemptive  
- All tasks share the same priority.  
- The **time‑slice** (quantum) determines when the CPU switches tasks.  
- A SysTick (timer interrupt) signals the end of the slice; the running task is re‑queued.  
- Overhead is $O(1)$.  

*Shortcoming:* No explicit deadline handling, so tasks may miss deadlines if the quantum is too large.

---

## 10.  Tidle Task & Bit‑Vector Queue Status  
- **Tidle** runs only when no ready task exists.  
- Scheduler keeps a **bit vector** of queue emptiness:  
  $$
  \text{bit}[p] = 1 \text{ if queue } p \text{ is nonempty, else } 0
  $$  
- Finding the next priority is $O(1)$ via a machine instruction (e.g., ARM CLZ).  
- Removing a task can be $O(n)$ worst case, but a bit vector keeps the search cheap.

---

## 11.  Scheduler Overhead & Storage  
- **Overhead**: decision time per tick is constant ($O(1)$).  
- **Storage**: For non‑preemptive EDF, store the execution order in an array of length  
  $$
  L = \sum_{i=1}^{n}\frac{\operatorname{lcm}}{T_i}
  $$  
  e.g., with LCM = 90, periods 18, 30, 45 →  
  $L = 90/18 + 90/30 + 90/45 = 5 + 3 + 2 = 10$.

---

## 12.  Key Takeaways (in a Nutshell)

- **Utilization** tells you how busy the CPU will be.  
- **RM**: fixed priorities, useful when deadlines ≈ periods, max ~69 % load.  
- **EDF**: dynamic priorities, optimal up to 100 % load.  
- **Non‑preemptive**: easier to implement, but may miss deadlines if not checked.  
- **Bit vectors** and **prime‑factor LCM** make scheduling efficient.  
- Always check **$U \le 1$** before trusting a schedule.

Use this cheat sheet to quickly verify schedulability, choose the right policy, and understand the trade‑offs between simplicity, overhead, and deadline guarantees.
