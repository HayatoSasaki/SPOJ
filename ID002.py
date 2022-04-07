# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/
# ITS FUCKING 1 BILLION NUMBERS, isPrime can't do this. Saving just because.

def isPrime(n2: int):
    isPrime = [True] * n2 
    isPrime[0] = False 
    isPrime[1] = False 
    for i in range(2, n2): # Save the primes in primeList.
        if isPrime[i]:
            primeList.append(i)
            for j in range(i*i, n2, i): # Set the multiples False.
                isPrime[j] = False

def output(m1,n1: int):
    if m1 == 1:
        m1 += 1
    isPrime(n1+1) # Fill the list of primes.
    for prime in range(len(primeList)): # Find the beginning.
        if primeList[prime] >= m1:
            break
    for prime in range(prime, len(primeList)): # Print the primes between m and n.
        print(primeList[prime])

# ------- Main.
global primeList
t = int(input()) # Number of testes.
for x in range(t): # Performs 't' tests.
    primeList = [] # Create/Reset the list of primes.
    m, n = [int(k) for k in input().split()] # Reads the range.
    output(m,n)
