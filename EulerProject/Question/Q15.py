'''
Created on 2018. 1. 10.

Lattice paths
Problem 15 
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?

Answer 137846528820
@author: sharb
'''

import numpy as np
dictCache = dict()

def countRoutes(m,n):
    if n == 0 or m ==0:
        return 1
    #return countRoutes(m, n-1) + countRoutes(m-1, n)
    if dictCache.get(str(m)+'x'+str(n) )== 0:
        return dictCache.get(str(m)+'x'+str(n))
    
    dictCache.setdefault(str(m)+'x'+str(n),countRoutes(m-1, n)+countRoutes(m, n-1))
    return dictCache.get(str(m)+'x'+str(n))

def countRoutesWithoutRecursive(m,n):   
    gGrid = np.zeros((m+1,n+1))
    
#     print(gGrid)
    for i in range(0,m+1):
        gGrid[i][0] = 1
#     print(gGrid)    
    for j in range(0,n+1):
        gGrid[0][j] = 1
#     print(gGrid)
    for i in range(1,m+1):
        for j in  range(1,n+1):
            gGrid[i][j] = gGrid[i-1][j] + gGrid[i][j-1]
#     print(gGrid)        
    return gGrid[m][n]
    
#print(str(countRoutes(3, 3)))
print(str(int(countRoutesWithoutRecursive(20, 20))))
