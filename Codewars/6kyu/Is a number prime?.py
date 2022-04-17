# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

from math import isqrt

def is_prime(num):
    if num < 3 or num % 2 == 0:
        if num == 2:
            return True
        return False
    for x in range(3, (isqrt(num)+1), 2):
        if num % x == 0:
            return False
    return True
