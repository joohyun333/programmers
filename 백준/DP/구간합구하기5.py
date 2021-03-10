# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
DP = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1,N+1):
    for j in range(1, N+1):
        DP[i][j] = arr[i-1][j-1]+DP[i-1][j]+DP[i][j-1]-DP[i-1][j-1]
for i in range(M):
    ax, ay, bx, by = map(int, input().split())
    a,b,c = (ax-1,by), (bx,ay-1), (ax-1,ay-1)
    print(DP[bx][by]-DP[a[0]][a[1]]-DP[b[0]][b[1]]+DP[c[0]][c[1]])