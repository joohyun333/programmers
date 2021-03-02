import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
DP = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(M + 1):
    for j in range(N + 1):
        if i == 0 | j==0:
            DP[i][j] = 1
        else:
            DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
result = ""
def solution(N, M, K):
    global result
    if N == 0:
        result += "z" * M
        return
    elif M == 0:
        result += "a" * N
        return
    elif DP[M][N-1] >= K:
        result += "a"
        solution(N - 1, M, K)
    elif DP[M][N-1] < K:
        result += "z"
        solution(N, M - 1, K - DP[M][N-1])


if DP[M][N] < K:
    print("-1")
else:
    solution(N, M, K)
    print(result)
