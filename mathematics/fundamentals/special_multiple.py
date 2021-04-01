#!/bin/python3

import os
import sys

def solve(n):
    for i in range(1,100000000000000):
        d = 9*int("{0:b}".format(i))
        if d%n==0:
            return d
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
