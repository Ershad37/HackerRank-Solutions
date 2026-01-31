# 🍎🍊 Apple and Orange Counter

This program solves the classic **“Apples and Oranges”** problem:  
given the positions of two fruit trees and a house on a number line, it counts how many apples and oranges fall on the house.

---

## 📌 Problem Description

A house is located on a number line between positions **`s`** and **`t`** (inclusive).

- An **apple tree** is at position **`a`**
- An **orange tree** is at position **`b`**

Each apple and orange falls a certain distance from its tree.  
Your task is to determine how many apples and how many oranges land on the house.

---

## 🧮 How It Works

For each fruit:

- The **final position** is calculated as:
  tree_position + fruit_distance

- If the final position lies between **`s`** and **`t`**, it is counted as landing on the house.

---

## 📥 Input Format

The program expects input from **standard input** in the following order:
    s t
    a b
    m n
    d1 d2 d3 ... dm
    e1 e2 e3 ... en


Where:
- `s t` → start and end of the house
- `a b` → apple tree and orange tree positions
- `m n` → number of apples and oranges
- `d` → distances each apple falls
- `e` → distances each orange falls

---

## 📤 Output Format

The program prints **two lines**:

1. Number of apples that land on the house  
2. Number of oranges that land on the house  

Example:
    1
    2


---

## 🛠 Example

### Input
  7 11
  5 15
  3 2
  -2 2 1
  5 -6


### Explanation
- Apples fall at positions:  
  `5 + (-2) = 3`, `5 + 2 = 7`, `5 + 1 = 6` → only `7` is in the house range
- Oranges fall at positions:  
  `15 + 5 = 20`, `15 + (-6) = 9` → only `9` is in the house range

### Output
  1
  1


---

## 🚀 How to Run

1. Save the file (e.g. `apples_and_oranges.py`)
2. Run in terminal:

```bash
python3 apple_and_orange.py
