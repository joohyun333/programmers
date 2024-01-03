from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
min_length = 2 * n
land_num = 1
for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            land_num += 1
            que = deque()
            que.append((i, j))
            land[i][j] = land_num

            while que:
                nowx, nowy = que.popleft()
                for k in range(4):
                    nx = nowx + dt[k][0]
                    ny = nowy + dt[k][1]
                    if 0 <= nx < n and 0 <= ny < n and land[nx][ny] == 1:
                        land[nx][ny] = land_num
                        que.append((nx, ny))

for i in range(n):
    for j in range(n):
        if land[i][j] != 0:
            que = deque()
            que.append((i, j, 0))
            target = land[i][j]
            chk = set()
            chk.add((i, j))
            while que:
                nowx, nowy, cost = que.popleft()
                if cost > min_length: continue
                for k in range(4):
                    nx = nowx + dt[k][0]
                    ny = nowy + dt[k][1]
                    if 0 <= nx < n and 0 <= ny < n and land[nx][ny] != target and (nx, ny) not in chk:
                        if land[nx][ny] != 0:
                            min_length = min(min_length, cost)
                        chk.add((nx, ny))
                        que.append((nx, ny, cost + 1))

print(min_length)