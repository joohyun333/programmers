# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
R, C = map(int, input().split())
forest = ['' for _ in range(R)]
water_queue = deque()
hedgehog = deque()
destination = ()
water_term = [[0 for _ in range(C)] for _ in range(R)]
water_visited = [[False for _ in range(C)] for _ in range(R)]
hedgehog_visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    forest[i] = input()
    for j in range(C):
        s = forest[i][j]
        if s == 'X':
            water_visited[i][j] = True
            hedgehog_visited[i][j] = True
        elif s == '*':
            water_queue.append((i, j, 0))
            hedgehog_visited[i][j] = True
        elif s == "S":
            hedgehog.append((i, j, 0))
        elif s == "D":
            water_visited[i][j] = True
            destination = (i, j)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while water_queue:
    y, x, z = water_queue.popleft()
    if not water_term[y][x]:
        water_visited[y][x] = True
        water_term[y][x] = z
        for i, j in direction:
            ny, nx = i + y, j + x
            if 0 <= ny < R and 0 <= nx < C and not water_visited[ny][nx]:
                water_queue.append((ny, nx, z + 1))
result = sys.maxsize
while hedgehog:
    y, x, z = hedgehog.popleft()
    if not hedgehog_visited[y][x]:
        hedgehog_visited[y][x] = True
        for i, j in direction:
            ny, nx = i + y, j + x
            if (ny, nx) == destination:
                result = min(result, z + 1)
            if 0 <= ny < R and 0 <= nx < C and not hedgehog_visited[ny][nx] and (water_term[ny][nx] > z+1 or water_term[ny][nx] == 0):
                hedgehog.append((ny, nx, z + 1))

print("KAKTUS" if result == sys.maxsize else result)