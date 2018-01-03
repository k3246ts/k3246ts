'''
Created on 2018. 1. 3.

Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer 31875000
@author: sharb
'''
for a in range(1, 1000):
    #print('a='+str(a)+' a^2='+str(a**2))
    for b in range(a+1,1000):
        #print('b='+str(b)+' b^2='+str(b**2))
        c = 1000 - a - b
        if c > 0 and a < b and b < c  :
            a2 = a**2
            b2 = b**2
            c2 = c**2-a2-b2
            if c2 == 0:
                #print('a='+str(a)+' b='+str(b)+' c='+str(c))
                print(a*b*c)

