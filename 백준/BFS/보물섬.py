from collections import deque
y,x = map(int, input().split())
graph = [list(input()) for _ in range(y)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False for _ in range(x)] for _ in range(y)]
answer = 0
for i in range(y):
    for j in range(x):
        if graph[i][j] == 'L':
            new_answer = 0
            visited = [[False for _ in range(x)] for _ in range(y)]
            visited[i][j] = True
            q = deque([[i, j, 0]])
            while q:
                qy, qx, q_distance = q.popleft()
                new_answer = max(new_answer, q_distance)
                for dx, dy in direction:
                    ny, nx = qy + dy, qx + dx
                    if 0 <= nx < x and 0 <= ny < y and not visited[ny][nx] and graph[ny][nx] == 'L':
                        visited[ny][nx] = True
                        q.append([ny, nx, q_distance + 1])
            answer = max(answer, new_answer)
print(answer)
