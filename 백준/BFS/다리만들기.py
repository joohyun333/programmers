#https://www.acmicpc.net/problem/2146
import copy
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
visited_sea = [[True for _ in range(N)] for _ in range(N)]
visited_island = [[0 for _ in range(N)] for _ in range(N)]
map_data = [[0 for _ in range(N) ] for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(N):
    map_data[i] = list(map(int, input().split()))
    for idx, j in enumerate(map_data[i]):
        if j == 1:
            visited_island[i][idx] = -1
        else:
            visited_sea[i][idx] = False


def group_dfs(i, j, group):
    q = deque()
    q.append((i, j))
    while q:
        y,x = q.popleft()
        for z in direction:
            next_y, next_x = y + z[0], x + z[1]
            if -1 < next_y < N and -1 < next_x < N and visited_island[next_y][next_x] == -1:
                visited_island[next_y][next_x] = group
                q.append((next_y, next_x))

group_count = 0
for i in range(N):
    for j in range(N):
        if map_data[i][j] == 1 and visited_island[i][j] == -1:
            group_count += 1
            visited_island[i][j] = group_count
            group_dfs(i, j, group_count)


def bfs(y, x, visited, group_num):
    q = deque()
    q.append((y,x,0))
    answer = sys.maxsize
    while q:
        y,x,d = q.popleft()
        if d > 2*N: continue
        for z in direction:
            next_y, next_x = y + z[0], x + z[1]
            if -1 < next_y < N and -1 < next_x < N and group_num != visited_island[next_y][next_x]:
                
                if not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    if map_data[next_y][next_x] == 0:
                        q.append((next_y,next_x,d+1))
                else:
                    if map_data[y][x] == 0 and map_data[next_y][next_x] == 1:
                        answer = min(answer, d)
    return answer

answer = sys.maxsize
for i in range(N):
    for j in range(N):
        if map_data[i][j] == 1 and visited_island[i][j] != 0:
            visited = copy.deepcopy(visited_sea)
            visited[i][j] = True
            result = bfs(i, j, visited, visited_island[i][j])
            answer = min(answer, result)
print(answer)