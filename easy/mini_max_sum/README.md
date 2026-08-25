# Mini-Max Sum

## Problem

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.

Print the minimum and maximum sums as two space-separated integers.

### Example

Given:

```text
1 2 3 4 5
```

The possible sums are:

```text
2 + 3 + 4 + 5 = 14
1 + 3 + 4 + 5 = 13
1 + 2 + 4 + 5 = 12
1 + 2 + 3 + 5 = 11
1 + 2 + 3 + 4 = 10
```

Therefore, the output is:

```text
10 14
```

## Approach

Instead of calculating all five possible sums, we can use the total sum of the array.

* The **minimum sum** is the total sum minus the largest number.
* The **maximum sum** is the total sum minus the smallest number.

For example:

```python
arr = [1, 2, 3, 4, 5]

total = sum(arr)

minimum = total - max(arr)
maximum = total - min(arr)
```

This avoids the need to sort the array.

## Solution

```python
def miniMaxSum(arr):
    total = sum(arr)

    minimum = total - max(arr)
    maximum = total - min(arr)

    print(minimum, maximum)
```

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Although the input contains exactly five integers, the solution works for any array size where the task is to exclude one element.

## Key Insight

The problem can be simplified by observing that every valid sum contains **four out of the five numbers**.

Therefore:

```text
Minimum = Total − Maximum Element
Maximum = Total − Minimum Element
```

This is more efficient than sorting the array first.

## HackerRank

**Problem:** Mini-Max Sum
**Platform:** HackerRank
**Difficulty:** Easy
