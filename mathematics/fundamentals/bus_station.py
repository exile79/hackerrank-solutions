#!/bin/python3

import os
import sys
import itertools  

# Complete the solve function below.
def solve(friendGroups):
    solutions = []
    totalFriends = sum(friendGroups)
    seatedTotal = 0
    minBusSeats = max(friendGroups)
    busSeats = 0

    # cumulative sum
    cumSum = set(itertools.accumulate(friendGroups))    
    
    for i in cumSum:
        
        if i < minBusSeats or totalFriends%i != 0:
            continue
        
        busSeats = i

        seatedFriends = 0
        seatedTotal = 0
        
        for idx, n in enumerate(friendGroups):
            seatedFriends += n
            if(seatedFriends > busSeats):
                break
            if(seatedFriends == busSeats):
                seatedTotal += n
                seatedFriends = 0
                if(seatedTotal == totalFriends):
                    solutions.append(busSeats)
                    break
                continue
            if(seatedTotal == totalFriends):
                solutions.append(busSeats)
                break
            seatedTotal += n
            
    solutions.sort()
    return solutions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
