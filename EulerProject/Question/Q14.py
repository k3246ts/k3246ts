'''
Created on 2018. 1. 9.

Longest Collatz sequence
Problem 14 
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Answer maxOfIndex : 837799 max : 525

@author: sharb
'''
import math

def getCollatzNum(iInput):
    if iInput == 1 :
        return iInput
    elif iInput % 2 == 0 :
        return iInput / 2
    else :
        return 3 * iInput + 1

iMap = [1 for _ in range(100)]
lst = [1 for _ in range(100)]

maxOfIndex = 0
max = 2
#get the list of Collatz
for i in range(2, 1000001):
    idx = i
    seq = 2
    while 1 != getCollatzNum(idx):
        seq = 1+ seq
        idx = getCollatzNum(idx)
    if max< seq:
        max = seq
        maxOfIndex = i

print('maxOfIndex : '+ str(maxOfIndex)+' max : '+str(max))    
    
