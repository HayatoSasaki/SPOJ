# PRIME1 - Prime Generator | https://www.spoj.com/problems/PRIME1/

t = int(input()) # Número de testes.

for x in range(t): # Realiza 't' testes.
    m, n = [int(m) for m in input().split()] # Recebe o intervalo.

    for m in range(m,n+1): # Checka o intervalo.
        if m > 1:
                for i in range(2,m+1): # Checka divisores individualmente.
                    if m == i:
                        print(m)
                        break
                    elif m % i == 0:
                        break
