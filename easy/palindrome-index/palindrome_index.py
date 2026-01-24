#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            l, r = left +1, right
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            if l >= r: return left
            
            l, r = left, right - 1
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            if l >= r: return right
            
            return -1
    return -1
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
