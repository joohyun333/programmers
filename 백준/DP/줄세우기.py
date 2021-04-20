# https://www.acmicpc.net/problem/2631
import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
DP = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(N -max(DP))