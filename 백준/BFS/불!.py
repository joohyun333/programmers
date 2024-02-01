import sys
from collections import deque
import copy
N, M = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False for _ in range(M)] for _ in range(N)]
fire_map = [[-1 for _ in range(M)] for _ in range(N)]
fire = deque()
jihun = deque()
for i in range(N):
    d = list(input())
    for j in range(M):
        if d[j] == "F":
            fire.append((i, j, 0))
        elif d[j] == "J":
            jihun.append((i, j, 0))
        elif d[j] == "#":
            visited[i][j] = True
v = copy.deepcopy(visited)
while fire:
    y, x, term = fire.popleft()
    v[y][x] = True
    fire_map[y][x] = term
    for dx, dy in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
            v[ny][nx] = True
            fire.append((ny, nx, term + 1))
v = copy.deepcopy(visited)
answer = sys.maxsize
while jihun:
    y, x, term = jihun.popleft()
    if (y == 0 or y == N - 1) or (x == 0 or x == M - 1):
        answer = min(answer, term+1)
        break
    v[y][x] = True
    for dx, dy in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not v[ny][nx] and (fire_map[ny][nx] == -1 or fire_map[ny][nx] > term + 1):
            v[ny][nx] = True
            jihun.append((ny, nx, term+1))
if answer == sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(answer)