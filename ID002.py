# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

from math import isqrt

def generator(m, n: int): 
    seg = [True] * (n-m+1) # Segment.
    r = isqrt(n)+1
    for lower in range(m,n+1): # Check in all numbers in range.
        if seg[n-lower]: 
            for factor in range(2,r):
                if lower % factor == 0:
                    for multi in range(lower, n+1, factor):
                        if lower > 3:
                            seg[multi-n] = False
    for p in range(m, n+1):
        if seg[p-n]:
            print(p)

def test(t): # Define test.
    for x in range(t): # Performs 't' tests.
        m, n = [int(i) for i in input().split()] # Reads the segment/range.
        if m < 2: # Skip [0, 1].
            m = 2
        generator(m,n)

test(int(input())) # Number of tests.
