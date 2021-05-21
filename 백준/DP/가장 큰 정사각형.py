# https://www.acmicpc.net/problem/1915
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(m+1)]+[[0]+list(map(int, input().strip('\n'))) for _ in range(n)]
for i in range(n+1):
    for j in range(m+1):
        if arr[i][j]:
            arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
print(max(sum(arr, [])) ** 2)