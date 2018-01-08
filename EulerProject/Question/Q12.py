'''
Created on 2018. 1. 8.

Highly divisible triangular number
Problem 12 
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Answer 76588876

@author: sharb
'''
import math

def getDivisor(n):
    divisorlst = []
    divisorlst.append(1)
#     print('n : ' + str(n))
    
    if n == 1 :
        return divisorlst
    elif n < 4:
        divisorlst.append(n)
        return divisorlst
    else:
        r = math.floor(math.sqrt(n))
        f = 2
        while f <= r:
            if n % f == 0 :
                divisorlst.append(f)
                divisorlst.append(int(n/f))
                
            f = f + 1
        divisorlst.append(n)
        r= list(set(divisorlst))
        r.sort()
        return r

lst = []
divisorlst = []
i = 1
lst.append(1)

while len(divisorlst) < 500:
#     print(lst)
    divisorlst = getDivisor(lst[len(lst) - 1])
#     print(divisorlst)
    lst.append(lst[len(lst) - 1] + i + 1)
    
    i = i + 1

print(str(lst[len(lst) - 1]))

print('end')