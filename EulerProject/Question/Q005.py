'''
Created on 2017. 8. 16.

Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer 232792560


@author: sharb
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

lcmNum = 1
for i in range(2,21):
    lcmNum = lcm(lcmNum,i)
    
print(lcmNum)