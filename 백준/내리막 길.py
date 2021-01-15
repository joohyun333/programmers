# # https://www.acmicpc.net/problem/1520
# import sys
# sys.setrecursionlimit(45000)
# input = sys.stdin.readline
# M, N = map(int, input().split())
# route = []
# for i in range(M):
#     route.append(list(map(int, input().split())))
# maps = [[0 for i in range(N)] for j in range(M)]
# count = 0
# def dfs(m, n, before=sys.maxsize):
#     if m < 0 or m > M - 1 or n < 0 or n > N - 1 or before <= route[m][n]:
#         return
#     elif m == M - 1 and n == N - 1:
#         maps[m][n] += 1
#         return True
#     else:
#         maps[m][n] += 1
#         before = route[m][n]
#         dfs(m - 1, n, before)
#         dfs(m + 1, n, before)
#         dfs(m, n - 1, before)
#         dfs(m, n + 1, before)
# dfs(0, 0)
# print(maps[M - 1][N - 1])
# -------------시간 초과----------------
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
h = []
ht = []
path = [[0] * n for i in range(m)]
path[0][0] = 1
for i in range(m):
    h.append([*map(int, input().split())])
    for j in range(n):
        ht.append((h[i][j], i, j))
ht.sort(reverse=True)
print(ht)
for (x, i, j) in ht:
    for (i1, j1) in filter(lambda t: t[0] in range(m) and t[1] in range(n),[(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]):
        if h[i1][j1] > x:
            path[i][j] += path[i1][j1]
print(path[m - 1][n - 1])
