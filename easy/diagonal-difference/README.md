# Description
This program calculates the absolute difference between the sums of the two diagonals in a square matrix.
It efficiently traverses the matrix to compute both diagonal sums in one pass.
# Problem Statement
Given a square matrix arr of size n x n, calculate the absolute difference between:
The sum of the primary diagonal (top-left to bottom-right).
The sum of the secondary diagonal (top-right to bottom-left).
Return the absolute difference as an integer.
Example:
arr = [
  [11, 2, 4],
  [4, 5, 6],
  [10, 8, -12]
]
Primary diagonal sum = 11 + 5 + (-12) = 4
Secondary diagonal sum = 4 + 5 + 10 = 19
Absolute difference = |4 - 19| = 15
