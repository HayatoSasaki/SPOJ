# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

global primeList

def sieve(n1: int):
    n1 += 1
    if n1 >= 2: # Se n == 1 nem se dá o trabalho.
        isPrime = [True] * n1 # Intervalo [0,n].
        isPrime[0] = False # Skippa 0.
        isPrime[1] = False # Skippa 1.
        for i in range(2, n1): # Marca os primes.
            if isPrime[i]:
                primeList.append(i)
                for j in range(i*i, n1, i): # Elimina os multiplos.
                    isPrime[j] = False
    return

def output(m2,n2: int):
    sieve(n2) # Guarda os primes até n via Simple Sieve.
    p = 0
    while m2 > primeList[p]: # Acha o começo.
        p += 1
    for pp in range(p,len(primeList)): # Printa os primes até n.
        print(primeList[pp])

# ------- Main.
t = int(input()) # Número de testes.
for x in range(t): # Realiza 't' testes.
    m, n = [int(i) for i in input().split()] # Recebe o intervalo.
    primeList = [] 
    output(m,n)
