# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

t = int(input()) # Número de testes.

def prime(p):
    i = 5 # Checker.

    if p == 1 : # Skippa o 1.
        return False
    if p == 2 or p == 3: # Prima o 2 e 3.
        return True
    if p % 2 == 0 or p % 3 == 0 : # Skippa divisíveis deles.
        return False
    while i*i <= p:
        if p % i == 0 or p % (i+2) == 0:
            return False
        i += 6 
    return True

for x in range(t): # Realiza 't' testes.
    m, n = [int(m) for m in input().split()] # Recebe o intervalo.

    for m in range(m,n+1): # Checka o intervalo.
        if prime(m): # Se retornar True, printa.
            print(m)
