# https://www.acmicpc.net/problem/14923
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
arr = []
wall = []
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        if a[j] == 1:
            wall.append((i, j))
    arr.append(a)
for i in wall:
    if