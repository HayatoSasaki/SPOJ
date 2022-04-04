# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

t = int(input()) # Número de testes.

def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return
    print(m)
    return

for x in range(t):
    m, n = input().split() # Recebe o intervalo.
    m = int(m) # Converte.
    n = int(n) # Converte.
          
    for m in range(m,n+1): # Checka o intervalo.
        if m > 1:
            prime(m)
