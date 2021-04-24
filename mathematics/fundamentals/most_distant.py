#!/bin/python3

import os
import sys
from math import sqrt

# Complete the solve function below.
def solve(coordinates):
    maxX, minX, maxY, minY = 0, 0, 0, 0
    
    for c in coordinates:
        minX=min(minX, c[0])
        maxX=max(maxX, c[0])
        minY=min(minY, c[1])
        maxY=max(maxY, c[1])
    
    d = [
        maxX-minX, 
        maxY-minY, 
        sqrt(maxX**2+maxY**2),
        sqrt(maxX**2+minY**2),
        sqrt(minX**2+maxY**2),
        sqrt(minX**2+minY**2)        
    ]
    
    return max(d)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
