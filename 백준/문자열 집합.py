import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = []
search = []
for i in range(N):
    S.append(input())
for i in range(M):
    search.append(input())
result = 0
for i in search:
    if i in S:
        result+=1
print(result)