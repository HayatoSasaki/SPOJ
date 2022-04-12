# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

from math import isqrt

def prime(p: int): # Prime checker.
    for test in range(3,isqrt(p)+1): # [3, √p]
        if p % test == 0:
            return False
    return True

# ---- main.
t = int(input()) # Number of tests.
for x in range(t): # Performs 't' tests.
    m, n = [int(i) for i in input().split()] # Reads the segment/range.
    if m <= 2: # Skips [0,1].
        print(2)
        m = 3
    elif m % 2 == 0: # m needs to be odd.
        m += 1
    for p in range(m,n+1,2): # Test the odd numbers in the segment/range.
            if(prime(p)): # Check if prime.
                print(p)
