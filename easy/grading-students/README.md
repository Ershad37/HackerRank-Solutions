# Grading Students

This project implements a solution to the **Grading Students** problem.

---

## 🧠 Problem Description

Given the grades of students, apply the following rounding rules:

1. Any grade less than 38 is a failing grade and is **not rounded**.
2. If the difference between a grade and the next multiple of 5 is **less than 3**, round the grade **up** to the next multiple of 5.
3. Otherwise, the grade remains the same.

### Example

| Grade | Rounded Grade |
|-------|---------------|
| 84    | 85            |
| 29    | 29            |
| 57    | 57            |

---

## 📁 Project Structure

└── grading_students.py # Main script with grading algorithm


---

## ⚡ Implementation Details

The algorithm works as follows:

1. Iterate through each student's grade.
2. If the grade is less than 38, leave it as-is.
3. If `grade % 5` is 3 or 4, round up to the next multiple of 5.
4. Return the modified list of grades.

### Time Complexity
- Iterates once over all grades → **O(n)**

### Space Complexity
- Modifies the list in place → **O(1)** extra space

---

## ▶ How to Run

This script reads input from standard input and writes output to a file defined by the environment variable `OUTPUT_PATH`.

### Example

```bash
export OUTPUT_PATH="output.txt"
python grading_students.py
