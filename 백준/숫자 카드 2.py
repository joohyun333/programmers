import sys
input = sys.stdin.readline
plus = [0]*10000001
minus = [0] * 10000001
N = int(input())
a = list(map(int, input().split()))
for i in a:
    if i>=0: plus[i]+=1
    else: minus[i]+=1
M = int(input())
b = list(map(int, input().split()))
for i in b:
    if i>=0: print(plus[i], end=' ')
    else: print(minus[i],end=' ')