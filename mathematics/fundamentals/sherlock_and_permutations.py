#!/bin/python3

import os
import sys

# solution found in https://www.xarg.org/puzzle/hackerrank/sherlock-and-permutations/

def noverkmodm(n, k, m):
    c = 1
    k = min([k, n - k])
    n = n - k;
    for i in range(1, k + 1):
        c = (c * ((n + i) % m) * pow(i, m - 2, m)) % m;
    return c

def solve(n, m):
    return noverkmodm(n + m - 1, n, 10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
