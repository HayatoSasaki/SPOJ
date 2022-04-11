# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/
# ITS FUCKING 1 BILLION NUMBERS, isPrime can't do this. Saving just because.

def isPrime(n2: int): # Define Simple Sieve.
    lp2 = [] # Create the list of primes.
    isPrime = [True] * n2 
    isPrime[0] = False 
    isPrime[1] = False 
    for i in range(2, n2): # Save the primes in primeList.
        if isPrime[i]:
            lp2.append(i)
            for j in range(i*i, n2, i): # Set the multiples False.
                isPrime[j] = False
    return lp2
from math import isqrt

def output(): 
    m, n = [int(i) for i in input().split()] # Reads the segment/range.
    lp = isPrime(n+1) # Fill the list of primes up to √n.
    if m == 1:
        m += 1
    for beginning in range(len(lp)): # Find the beginning.
        if lp[beginning] >= m:
            break
    for prime in range(beginning, len(lp)): # Print the primes between m and n.
        print(lp[prime])
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
        output()
        m, n = [int(i) for i in input().split()] # Reads the segment/range.
        if m < 2: # Skip [0, 1].
            m = 2
        seg_sieve(m,n)

test(int(input())) # Number of tests.
