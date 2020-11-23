# https://www.acmicpc.net/problem/14889
from itertools import combinations
import copy
import sys
n = int(input())
S = [list(map(int, input().split(" "))) for i in range(n)]
for i in range(n):
    for j in range(n):
        S[j][i] = S[i][j]+S[j][i]
        S[i][j] = 0
start = combinations(range(n),n//2)
link = [tuple(set(range(n)) - set(i)) for i in copy.copy(start)]
min_point = sys.maxsize
for x, y in zip(start, link):
    start_t = sum(S[i][j] for i, j in combinations(x, 2))
    link_t = sum(S[i][j] for i, j in combinations(y, 2))
    if abs(start_t - link_t) < min_point:
        min_point = abs(start_t-link_t)
print(min_point)
