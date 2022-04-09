# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

from math import isqrt

def sieve(n: int, list_prime: list): # Define Simple Sieve.
    list_tester = [True] * n
    r = isqrt(n)+1
    for i in range(2, r):
        if list_tester[i]:
            list_prime.append(i) # Save the primes in the list.
            for j in range(i*i, r, i): # Set the multiples False.
                list_tester[j] = False

def seg_sieve(m,n: int): # Define Segmented Sieve.
    list_prime = [] # Create the list of primes.
    sieve(n+1, list_prime) # Fill the list with primes up to √n.
    seg = [True] * (n-m+1) # Segment.
    
    for chibi in range(m,n+1): # Smallest divisor of a prime in the range.
            if seg[chibi-n]:
                for prime in list_prime: # 2, 3, 5, 7, 11,...
                    if chibi % prime == 0:
                        for multi in range(chibi, n+1, prime):
                            if chibi > 3:
                                seg[multi-n] = False
    for i in range(m, n+1):
        if seg[i-n]:
            print(i)

def test(t): # Define test.
    for x in range(t): # Performs 't' tests.
        m, n = [int(i) for i in input().split()] # Reads the segment/range.
        if m < 2: # Skip [0, 1].
            m = 2
        seg_sieve(m,n)

test(int(input())) # Number of tests.
