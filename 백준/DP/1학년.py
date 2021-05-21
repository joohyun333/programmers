# https://www.acmicpc.net/problem/5557
N = int(input())
arr = list(map(int, input().split()))
result = arr[N - 1]
arr = arr[:N - 1]
DP = [[0] * 21 for _ in range(N-1)]
DP[0][arr[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if DP[i - 1][j]>0:
            a, b = j + arr[i], j - arr[i]
            if 0 <= a <= 20:
                DP[i][a] += DP[i-1][j]
            if 0 <= b <= 20:
                DP[i][b] += DP[i-1][j]
print(DP[N-2][result])
