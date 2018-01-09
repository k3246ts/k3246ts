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
import time
t=time.time()

nums = {1:1}
nums_cur = {}
# n - number we start to count until 1, cur - current number, count - current item number
n=1
cur=1
count=1
max=0
while n < 1000000:
    #if not n%100000: print 'n=', n
    #print 'n='+str(n), 'cur='+str(cur), 'count='+str(count), 'max='+str(max)
    if cur in nums:
        tmp=count+nums[cur]
        if tmp-1 > max:
            print ('New max:', tmp-1, 'num:', n, time.time()-t)
            max=tmp-1
        for i in nums_cur.keys():
            nums[i]=nums[cur]+count-nums_cur[i]
        nums_cur={}
        # Increase n until it doesn't appear in the checked-numbers array
        while n in nums:
            n+=1
        cur=n
        count=1
    nums_cur[cur]=count
    count+=1
    if cur%2: cur=3*cur+1
    else: cur/=2
print ('Done.', time.time()-t)