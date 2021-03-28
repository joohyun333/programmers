# https://www.acmicpc.net/problem/14658
import sys, itertools

input = sys.stdin.readline
N, M, L, K = map(int, input().split())  # 가로 세로
arr = []
for i in range(K):
    a, b = map(int, input().split())  # 가로 세로
    arr.append((b, a))  # 세로 가로

result = 0
for i, j in itertools.combinations_with_replacement(range(K),2):
    min_y = min(arr[i][0], arr[j][0])
    min_x = min(arr[i][1], arr[j][1])
    total = 0
    for z in arr:
        if min_y<=z[0]<=min_y+L and min_x<=z[1]<=min_x+L:
            total+=1
    if result < total:
        result = total
print(K - result)
