# https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
DP = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
dist = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    DP[a][b] = min(c, DP[a][b])
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            DP[i][i] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for z in range(1, n + 1):
            DP[j][z] = min(DP[j][z], DP[j][i] + DP[i][z])

for i in range(1,n+1):
    for j in range(1,n+1):
        if DP[i][j] == sys.maxsize:
            DP[i][j] = 0

for i in DP[1:]:
    print(' '.join(map(str,i[1:])))