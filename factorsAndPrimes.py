# this file contains two functions, one returns a list of all factors of the input number
# the seconed uses the first one and says if the length of the returned list is only two,
# then the number must be prime and is added to the list of primes

# the second function is set to gather up a list of primes under a set number


# This is a function that return a list of factors for a number

def factor(numberToFactor):
    factors = []
    for i in range(1, numberToFactor + 1):
        if numberToFactor % i == 0:
            factors.append(i)
    return factors

# all the numbers that are prime under a certain limit
# using our previous function, a prime factor returns a list of the length 2
# so if the function returns a list of length two when given the number then it is prime

def primeFactors(limit):
    primeList = []
    for i in range(1, limit + 1):
        num = factor(i)
        if len(num) == 2:
            primeList.append(i)
    return primeList

print(factor(600851475143))
