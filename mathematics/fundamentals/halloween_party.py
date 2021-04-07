#!/bin/python3

import os
import sys

#
# Complete the halloweenParty function below.
#
def halloweenParty(k):
    m = k%2
    d = int(k/2)
    n = d*(d+m)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        k = int(input())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
