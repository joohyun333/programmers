N, M = map(int, input().split())
MB = [0]+list(map(int, input().split()))
cost = [0]+list(map(int, input().split()))
DP = [[0]*(sum(cost)+1) for _ in range(N+1)]
result = sum(cost)
for i in range(1, N+1):
    b = MB[i]
    c = cost[i]
    for j in range(1, sum(cost)+1):
        if j < c:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], b+DP[i-1][j-c])
        if DP[i][j]>=M:
            result = min(result, j)
for i in DP:
    print(i)
print(result)