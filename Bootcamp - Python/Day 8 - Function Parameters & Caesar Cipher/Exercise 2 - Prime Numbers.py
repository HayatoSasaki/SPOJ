from math import isqrt

def prime_checker(num):
    if num < 3 or num % 2 == 0:
        if num == 2:
            return True
        return False
    for x in range(3, (isqrt(num)+1), 2):
        if num % x == 0:
            return False
    return True

if(prime_checker(int(input("Check this number: ")))):
    print("It's a prime number.")
else:
    print("It's not a prime number.")