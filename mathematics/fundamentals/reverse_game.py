#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for tt in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        if k < int(n/2):
            print(1 + k*2)
        else:
            print((n-1-k)*2)        
        
