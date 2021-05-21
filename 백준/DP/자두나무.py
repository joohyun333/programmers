# https://www.acmicpc.net/problem/2240
import sys, collections

T, W = map(int, input().split())
arr = [0] + [int(input()) for i in range(T)]
DP = [[[0] * 3 for _ in range(T + 1)] for _ in range(W + 1)]
for i in range(1, T + 1):
    for j in range(1, W + 1):
        if arr[i] == 1:
            DP[1][i][j] = max(DP[1][i - 1][j] + 1, DP[2][i - 1][j - 1] + 1)
            DP[2][i][j] = max(DP[1][i - 1][j - 1], DP[2][i - 1][j])
        else:
            if i == 1 and j == 1:
                continue
            else:
                DP[1][i][j] = max(DP[2][i - 1][j - 1], DP[1][i - 1][j])
                DP[2][i][j] = max(DP[1][i - 1][j - 1] + 1, DP[2][i - 1][j] + 1)
ans = 0
for i in range(1, W+1):
    ans = max(ans, max(DP[1][T][i], DP[2][T][i]))
    print(ans)
for i in DP:
    print(i)
