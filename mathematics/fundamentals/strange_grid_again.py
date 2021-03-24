#!/bin/python3

import os
import sys

#
# Complete the strangeGrid function below.
#
def strangeGrid(r, c):
    return 10*max(0, int((r-1)/2)) + 2*(c-1) + (r-1)%2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
