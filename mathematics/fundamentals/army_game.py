#!/bin/python3

import os
import sys
from math import ceil

def gameWithCells(n, m):
    return ceil(m/2)*ceil(n/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
