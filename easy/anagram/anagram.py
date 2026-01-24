#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    count = 0
    if len(s) % 2 == 0:
        n = len(s) // 2
    else:
        return -1
    
    first_half = {}
    second_half = {}
    
    for i in range(n):
        if s[i] not in first_half:
            first_half[s[i]] = 1
        else:
            first_half[s[i]] += 1
    
    for j in range(n, n + n):
        if s[j] not in second_half:
            second_half[s[j]] = 1
        else:
            second_half[s[j]] += 1
    
    for char in first_half.keys():
        if char in second_half.keys() and first_half[char]>second_half[char]:
            count += first_half[char] - second_half[char]
        elif char not in second_half:
            count += first_half[char]
        else:
            pass

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()