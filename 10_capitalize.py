#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        # ["i", "am", "buddhika", "weerasinghe"]
        # ["I", "Am", "Buddhika", "Weerasinghe"]
        # I is replaced with capital 
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    # [I am buddhika weerasinghe]

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
