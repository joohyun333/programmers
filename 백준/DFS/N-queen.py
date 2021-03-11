import sys

N = int(input())
input = sys.stdin.readline


def dfs(n):
    global result, col, diag1, diag2
    if n == N:
        result += 1
        return
    for i in range(N):
        if not (col[i] or diag1[i + n] or diag2[i - n + N - 1]):
            col[i] = diag1[i + n] = diag2[i - n + N - 1] = True
            dfs(n + 1)
            col[i] = diag1[i + n] = diag2[i - n + N - 1] = False


result = 0
col, diag1, diag2 = [False] * N, [False] * (N * 2 - 1), [False] * (N * 2 - 1)
dfs(0)
print(result)
