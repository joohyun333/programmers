# #https://www.acmicpc.net/problem/9020
import sys
N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
n=max(nums)
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for i in nums:
    min_d = sys.maxsize
    s = e = max([primes.index(x) for x in primes if x<=i/2])
    while s>=0 and e<=len(primes)-1:
        if primes[s]+primes[e] > i:
            s-=1
        elif primes[s]+primes[e] < i:
            e+=1
        elif primes[s]+primes[e] == i:
            print(str(primes[s])+" "+str(primes[e]))
            break