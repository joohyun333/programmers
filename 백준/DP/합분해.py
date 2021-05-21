# https://www.acmicpc.net/problem/2225
N, K = map(int, input().split())
DP = [[0] *(N+1) for _ in range(K+1)]
DP[0][0] = 1
for i in range(1, K+1):
    for j in range(N+1):
        DP[i][j] = (DP[i][j-1]+DP[i-1][j])%1000000000
print(DP[K][N])
for i in DP:
    print(i)