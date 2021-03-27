#!/bin/python3

import os
import sys
import math
#
# Complete the divisors function below.
#
def divisors(n):
    cnt = 0
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if (n % i == 0) :
             
            if i % 2 == 0:
                cnt = cnt + 1
                
            divu = n / i
            if (divu != i and divu % 2 == 0):
                cnt = cnt + 1
            

    if n % 2 == 0:
        cnt = cnt + 1                
    return cnt
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
