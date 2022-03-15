# this was originally my solution to project euler number 3 that I learned from the link below. 
# this file contains an algorithm that returns the largest prime factor if there is one, if the 
# algorithm does not return anything then that number is prime
# the number being factored is = to the <number> var. this can either just be changed or this can be 
# really easily just put into a funciton.

# https://levelup.gitconnected.com/solve-and-understand-the-project-euler-problems-in-python-introduction-and-problems-1-3-32625d1633f7
import math

number = 1073

for prime_factor in range(2, int(math.sqrt(number)) + 1): # you only have to go up to the square root
    while number % prime_factor == 0:
        number = number / prime_factor
        if number == 1 or number == prime_factor:
            print(prime_factor)
            break
