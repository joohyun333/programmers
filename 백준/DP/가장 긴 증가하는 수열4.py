# https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
DP = [1 for _ in range(N)]
DP_arr = [[i] for i in arr]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            if DP[i] < DP[j]+1:
                DP_arr[i] = DP_arr[j] + [arr[i]]
                DP[i] = DP[j]+1
result = 0
result_arr = 0
for i,e in enumerate(DP):
    if e>result:
        result = e
        result_arr = DP_arr[i]
print(result)
print(' '.join(map(str, result_arr)))