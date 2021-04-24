#!/bin/python3

import os
import sys

def nn(num, base):
    ret = 0
    # print('num',num,'base',base)
    denom = num % 10
    if denom >= base:
        return 0
    nom = num // 10    
    ret = denom  # multi by base**0
    pw = 1
    while nom != 0:
        denom = nom % 10
        
        if denom >= base:
            return 0
        
        nom = nom // 10
        ret = ret + denom * base**pw
        pw = pw + 1
    
    return ret

def ff(n):
    return n*(n-1)//2

def solve(dates):
    sdecs = [nn(n[1],n[0]) for n in dates]
    sset = set(sdecs)
    if 0 in sset:
        sset.remove(0)
    cnts = [sdecs.count(t) for t in sset]
    fcnts = list(map(ff,cnts))
    c = sum(fcnts)
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    dates = []

    for _ in range(n):
        dates.append(tuple(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
