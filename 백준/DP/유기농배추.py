import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    M, N, K = map(int, input().split())
    discovered = [[True] * M for _ in range(N)]
    go = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(K):
        a, b = map(int, input().split())
        discovered[b][a] = False


    def dfs(i, j):
        stack = [(i, j)]
        while stack:
            n, m = stack.pop()
            if not discovered[n][m]:
                discovered[n][m] = True
                for gx, gy in go:
                    if 0 <= n+gx < N and 0 <= m+gy < M:
                        stack.append([n+gx, m+gy])
        return
    count = 0
    for i in range(N):
        for j in range(M):
            if not discovered[i][j]:
                dfs(i, j)
                count += 1
    print(count)
