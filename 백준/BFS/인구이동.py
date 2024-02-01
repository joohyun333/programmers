import math
from collections import deque
N, L, R = map(int, input().split())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    is_not_move = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                move_count = 0
                move_sum = 0
                route = set()
                q = deque([[i, j]])
                while q:
                    y, x = q.popleft()
                    move_sum += graph[y][x]
                    route.add((y, x))
                    move_count += 1
                    for dx, dy in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                            visited[ny][nx] = True
                            q.append([ny, nx])
                if move_count > 1:
                    is_not_move = False
                    avg = math.floor(move_sum / move_count)
                    answer += 1
                    for ry, rx in route:
                        graph[ry][rx] = avg
    if is_not_move:
        print(answer)
        break