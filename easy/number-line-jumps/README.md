# 🦘 Kangaroo Meeting Problem

This program solves the **Kangaroo Problem**, where two kangaroos jump forward on a number line at different speeds. The goal is to determine whether they will ever land on the **same position at the same time**.

---

## 📖 Problem Description

You are given four integers:

- `x1` – starting position of kangaroo 1  
- `v1` – jump distance of kangaroo 1  
- `x2` – starting position of kangaroo 2  
- `v2` – jump distance of kangaroo 2  

Both kangaroos jump in the **positive direction** (toward infinity).  
After each jump, their positions increase by their respective jump distances.

Your task is to decide whether there exists some number of jumps such that both kangaroos land at the **same location**.

If they do, print:
  YES
otherwise, print:
  NO
  
---

## 🧠 How It Works

The idea is based on:

- If one kangaroo starts ahead and jumps faster (or the same speed), the other can never catch up.
- Otherwise, we check whether the difference in their starting positions can be eliminated by the difference in their jump distances.

This avoids simulating every jump and makes the solution very fast.

---

## 🧾 Input Format

A single line of four space-separated integers:
x1 v1 x2 v2

### Example
0 3 4 2

---

## 📤 Output Format

A single line containing either:
YES
or 
NO

---

## ✅ Example

**Input**
0 3 4 2

**Output**
YES

Explanation:  
After 4 jumps, both kangaroos reach position 12.

---

**Input**
0 2 5 3

**Output**
NO

Explanation:  
The second kangaroo starts ahead and jumps faster, so the first one can never catch up.

---

## 🚀 How to Run

1. Save the script as `kangaroo.py`
2. Run the program:
   ```bash
   python3 number_line_jumps.py


