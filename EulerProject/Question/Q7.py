'''
Created on 2018. 1. 3.

10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer 104743

@author: sharb
'''

import math

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0 :
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else :
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r :
            if n % f == 0 :
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6

        return True

limit = 10001
count = 1
candidate = 1
while True:
    candidate = candidate + 2
    if isPrime(candidate):
        count = count + 1
    if count == limit:
        break

print(candidate)
