# https://www.acmicpc.net/problem/13305
# 21:48
import sys

input = sys.stdin.readline
N = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
min_cost = sys.maxsize
for i in range(1, N):
    if min_cost > cost[i - 1]:
        min_cost = cost[i - 1]
    result += (dis[i - 1] * min_cost)
print(result)
