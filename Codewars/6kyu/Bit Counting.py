# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 

def count_bits(n):
    return str(bin(n)).count('1') # bin(n).count("1") would have worked.
