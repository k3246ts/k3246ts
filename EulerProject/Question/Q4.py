'''
Created on 2017. 7. 26.

Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer 4
906609

@author: sharb
'''

# print(max([x*y for x in range(999,900,-1) for y in range(x,900,-1) if str(x*y) == str(x*y)[::-1]]))

def PE004(n=3):
  pMax, deuxX1 = 0, 0
  for tot in range(2*10**n - 2, 2*10**(n-1) - 1, -1):
    for i in range(10**n-1, (tot-1)//2, -1):
      p=i*(tot-i)
      if pMax<p:
        s=str(p)
        if s==s[::-1]:
          pMax=p
          print(pMax)
          deuxX1=max(deuxX1, 2*(tot-i))
    if tot<=deuxX1: return pMax

def PE004_2(n=3):
  F=[ [(3,3), (7,7), (9,1)] ]
  i=0
  e=1
  E=10
  fin=10**(n//2) # ça suffit
  while E<fin:
    i+=1
    e=E
    E*=10
    tmp=[]
    for x,y in F[i-1]:
      for c in range(0,E,e):
        for d in range(0,c+1,e):
          if not ((c+x)*(d+y)+1)%E:
            tmp.append((c+x, d+y))
    F.append(tmp)
  flag=False
  for i in range(n//2):
    M1=10**n-10**(n-n//2+i)
    M2=10**(n//2-i)
    #F[-(1+i)].sort(key=sum, reverse=True)
    mini=0
    res=0
    for tot in range(2*10**(2*i+1)-2, -1, -1):
      if tot<mini: return res
      for d in range(10**(2*i+1)-1, (tot-1)//2, -1):
        c=tot-d
        for x,y in F[-(1+i)]:
          X=M1+c*M2+x
          Y=M1+d*M2+y
          
          if len(str(X)) != n:
              continue
          
          if len(str(Y)) != n:
              continue
          
          p=str(X*Y)
          if p==p[::-1]:
            print(X,Y,X*Y)
            res=max(X*Y, res)
            mini=max(mini, 2*c)

PE004_2(6)