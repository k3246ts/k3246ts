'''
Created on 2017. 7. 26.

Largest prime factor
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer 3
6857

@author: sharb
'''

number = 600851475143
i = 2
m = 2
while number != 1:
    if number % i == 0:
        number = number / i
        m = i
    i = i + 1

print (m)