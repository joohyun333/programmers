# https://www.acmicpc.net/problem/13458
import collections
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = collections.defaultdict(int)
for i in set(A):
    result[i] = 1
    e = i
    e-=B
    if e :
        while e>0:
            e -= C
            result[i]+=1
answer = 0
for i in A:
    answer+=result[i]
print(answer)
