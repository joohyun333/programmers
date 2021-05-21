# https://www.acmicpc.net/problem/16236
import heapq, collections, sys

N = int(input())
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

fishs = [[] for _ in range(6)]
start = [0, 0]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j]
        if 0 < arr[i][j] < 7:
            fishs[arr[i][j]].append((i, j))

baby_shark = 2
total_time = 0
remove_count = 0
spots = (0, start[0], start[1])
dis = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(fishs, spots)
while remove_count < baby_shark - 1 and fishs[baby_shark - 1]:
    discoverd = [[False] * N for _ in range(N)]
    queue = [(0, spots[1], spots[2])]
    next_spot = (sys.maxsize, 21, 21)
    eat_fish = []
    while queue:
        d, y, x  = queue.pop(0)
        if arr[y][x] == baby_shark - 1:
            eat_fish.append((d, y, x))
            if len(eat_fish) == baby_shark-1 :
                break
        for i, j in [(i + y, j + x) for i, j in dis if 0 <= i + y < N and 0 <= j + x < N]:
            if arr[i][j]<baby_shark-1:
                queue.append((d+1, i, j))
        print(next_spot)
    total_time += next_spot[0]
    fishs[baby_shark - 1].remove((next_spot[1], next_spot[2]))
    spots = next_spot
    remove_count += 1
    if remove_count == baby_shark - 1:
        remove_count = 0
        baby_shark += 1
print(total_time)
