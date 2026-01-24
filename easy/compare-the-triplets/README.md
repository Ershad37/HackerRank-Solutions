# Description
This program compares two triplets of integers and awards points based on element-wise comparisons.
It returns a two-element array representing the points for each participant.
# Problem Statement
Alice and Bob each have triplets of scores: a = [a0, a1, a2] and b = [b0, b1, b2].
For each index i:
If a[i] > b[i], Alice receives 1 point.
If a[i] < b[i], Bob receives 1 point.
If a[i] == b[i], neither receives a point.
Return a list [alice_points, bob_points] representing their scores.
Example:
Input: a = [5, 6, 7], b = [3, 6, 10]
Output: [1, 1]
Explanation:
Compare index 0: 5 > 3 → Alice +1
Compare index 1: 6 == 6 → No points
Compare index 2: 7 < 10 → Bob +1
