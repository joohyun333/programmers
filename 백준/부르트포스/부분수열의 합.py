import sys
from itertools import combinations
input = sys.stdin.readline

N, S=  map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(1,N+1):
    m = list(map(list,combinations(arr,i)))
    for i in m:
        if S == sum(i): result+=1
print(result)