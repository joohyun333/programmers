#https://www.acmicpc.net/problem/2468
from collections import deque
N = int(input())
graph = []
max_h = 0
for _ in range(N):
    a = list(map(int, input().split()))
    max_h = max(max_h, max(a))
    graph.append(a)
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
h = 1
answer = 0
while h <= max_h:
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= h and not visited[i][j]:
                count += 1
                d = deque()
                visited[i][j] = True
                d.append((i, j))
                while d:
                    y, x = d.popleft()
                    for dy, dx in direction:
                        new_y, new_x = dy + y, dx + x
                        if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and graph[new_y][new_x] >= h:
                            visited[new_y][new_x] = True
                            d.append((new_y, new_x))
    answer = max(answer, count)
    h += 1
print(answer)