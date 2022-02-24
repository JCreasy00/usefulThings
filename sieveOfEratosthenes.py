# my notes on the Sieve of Eratosthenes (SOE)
# which is an algorithm that finds primes

# Finds prime numbers under a certain number using the SOE
from math import isqrt # import square root function instead of making one


def primesLessThan(n):
    if n <= 2:
        return []
    primes = [True] * n
    primes[0] = False
    primes[1] = False


    for i in range(2,isqrt(n)): # the range does not include all numbers, only 2-square root of limit num
        # if true we mark out all multiples of that number that are bigger than that number (i)
        if primes[i]:
            for x in range(i*i, n, i): # range(i*i, n, i): start at square of i (any factor less than i has been marked out), go to n, start at i*i, go to n at a jump of i = multiples of i
                primes[x] = False
    # return all i in range(n) if i is true (anything still left to be true )
    return [i for i in range(n) if primes[i]]


print(primesLessThan(100))