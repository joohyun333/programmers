# https://www.acmicpc.net/problem/15686
import itertools
import sys

N, M = map(int, input().split())
chi = []
home = []
for i in range(N):
    d = list(map(int, input().split()))
    for j in range(N):
        if d[j] == 1:
            home.append((i, j))
        elif d[j] == 2:
            chi.append((i, j))
cases = list(itertools.combinations(chi, M))
answer = sys.maxsize
for case in cases:
    ch_answer = 0
    for h in home:
        min_dis = 101
        for c in case:
            min_dis = min(min_dis,(abs(c[0] - h[0]) + abs(c[1] - h[1])))
        ch_answer += min_dis
    answer = min(answer, ch_answer)
print(answer)