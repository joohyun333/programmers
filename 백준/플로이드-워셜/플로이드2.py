# https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
DP = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
dist = [[] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        dist[i].append([i])
for i in range(m):
    a, b, c = map(int, input().split())
    if DP[a][b] > c:
        DP[a][b] = c
        if len(dist[a][b])>1:
            dist[a][b].pop()
        dist[a][b].append(b)

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            DP[i][i] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for z in range(1, n + 1):
            a, b = DP[j][z], DP[j][i] + DP[i][z]
            if a > b:
                DP[j][z] = DP[j][i] + DP[i][z]
                dist[j][z] = dist[j][i] + dist[i][z][1:]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if DP[i][j] == sys.maxsize:
            DP[i][j] = 0

for i in DP[1:]:
    print(' '.join(map(str, i[1:])))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j :
            print(0)
        else:
            print(str(len(dist[i][j])) + " " + ' '.join(map(str, dist[i][j])))
