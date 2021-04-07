#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isFibo' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isFibo(n):
    n = 5*n**2
    return 'IsFibo' if math.sqrt(n+4)%1==0 or math.sqrt(n-4)%1==0 else 'IsNotFibo'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = isFibo(n)

        fptr.write(result + '\n')

    fptr.close()
