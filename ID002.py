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

def test(t): # Define test.
    for x in range(t): # Performs 't' tests.
        output()

test(int(input())) # Number of tests.
