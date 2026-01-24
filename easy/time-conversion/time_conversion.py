#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour, minutes, seconds = s.split(":")
    time = ""
    for char in seconds:
        if char.isalpha():
            time += char
            seconds = seconds.replace(char, "")
    hour, minutes, seconds = int(hour), int(minutes), int(seconds)
    
    if time == "AM" and hour == 12:
        hour = 00
    elif time == "PM" and hour != 12:
        hour += 12
        
    return f"{hour:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
