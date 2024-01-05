# https://www.acmicpc.net/problem/1106
import sys

C, N = map(int, input().split())
dp = [sys.maxsize for _ in range(C + 101)]
dp[0] = 0
cost_count_list = []
for i in range(N):
    cost, count = map(int, input().split())
    multiple = count
    while multiple <= C + 100:
        dp[multiple] = min(dp[multiple], dp[multiple - count] + cost)
        multiple += 1
print(min(dp[C:]))