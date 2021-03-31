#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr, queries):
    r = []
    for q in queries:
        if q[0] > q[1]:  
            r.append('Odd') # it is one (odd)
        elif q[0] != q[1] and arr[q[0]]==0:
            r.append('Odd') # next num is 0 and indices are different, so it is one (odd)
        elif arr[q[0]-1] % 2 != 0:
            r.append('Odd')
        else:
            r.append('Even')            
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
