# # https://www.acmicpc.net/problem/2056
import sys

input = sys.stdin.readline
N = int(input())
tail = [0] * (N + 1)
tail_node = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
for i in range(1, N + 1):
    t, n, *node = map(int, input().split())
    time[i] = t
    tail_node[i] = node

for i in range(1, N + 1):
    temp = 0
    for j in tail_node[i]:
        temp = max(temp, time[j])
    time[i] += temp
print(max(time))