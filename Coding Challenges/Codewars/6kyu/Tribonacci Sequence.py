# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
# Create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

def tribonacci(signature, n):    
    for t in range(n-3):
        signature.append(signature[t]+signature[t+1]+signature[t+2])
    return [tribonacci_ for tribonacci_ in signature[0:n]]
