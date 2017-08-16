'''
Created on 2017. 8. 16.

Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer 25164150

http://mathbang.net/628

@author: sharb
'''

num = 100
temp = 0
diff = 0

temp =  num ** 2
diff = (3 * temp ** 2 + 2 * temp * num - 3 * temp -2 * num )/12

print(diff)