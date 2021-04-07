#!/bin/python3

import os
import sys
from math import factorial

def solve(n, k):
    d = factorial(n+k-1) // (factorial(k)*factorial(n-1))
    return d % 10**9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        k = int(input())

        result = solve(n, k)
        fptr.write(str(result)+'\n')

    fptr.close()
