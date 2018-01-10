'''
Created on 2018. 1. 3.

Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer 142913828922
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
    
print(sum([x for x in range(2000000) if isPrime(x)]))