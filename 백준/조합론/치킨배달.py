import itertools
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
chicken = []
house = []
for n in range(N):
    for index, spot in enumerate(list(map(int, input().split()))):
        if spot == 1:
            house.append((n, index))
        elif spot == 2:
            chicken.append((n, index))

ch = list(itertools.combinations(chicken, M))
min_dis = sys.maxsize
for chickens in ch:
    route = []
    close_dis = 0
    for h in house:
        max_close_by_house = []
        for c in chickens:
            dis = abs(h[0]-c[0])+abs(h[1]-c[1])
            max_close_by_house.append(dis)
        close_dis+= sorted(max_close_by_house)[0]
    if min_dis>close_dis: min_dis = close_dis
print(min_dis)