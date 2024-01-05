# https://www.acmicpc.net/problem/10026
from collections import deque
N = int(input())
color = {"RED": 0, "GREEN": 0, "BLUE": 0}
color_2 = {"RED": 0, "GREEN": 0, "BLUE": 0}
data = ["" for _ in range(N)]
data_2 = ["" for _ in range(N)]
dt = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    d = input()
    data[i] = d
    data_2[i] = d.replace("G", "R")
def bfs (i, j, color_str, is_red_green):
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        for d in dt:
            new_y, new_x = y + d[0], x + d[1]
            if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x]:
                if not is_red_green:
                    if data[new_y][new_x] == color_str:
                        visited[new_y][new_x] = True
                        q.append((new_y, new_x))
                else:
                    if data_2[new_y][new_x] == color_str:
                        visited[new_y][new_x] = True
                        q.append((new_y, new_x))


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            if data[i][j] == "R":
                color["RED"] += 1
            if data[i][j] == "G":
                color["GREEN"] += 1
            if data[i][j] == "B":
                color["BLUE"] += 1
            bfs(i, j, data[i][j], False)

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            if data_2[i][j] == "R":
                color_2["RED"] += 1
            if data_2[i][j] == "B":
                color_2["BLUE"] += 1
            bfs(i, j, data_2[i][j], True)

print(str(sum(color.values())) + " " + str(sum(color_2.values())))
