# https://www.acmicpc.net/problem/14502
from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
data = []
virus = deque()
safe_count = 0
safe = set()
for i in range(n):
    a = list(map(int, input().split()))
    data.append(a)
    for j in range(m):
        if a[j] == 2:
            virus.append([i,j])
        elif a[j] == 0:
            safe.add((i, j))
            safe_count += 1

c = list(combinations(safe, 3))
direction = [[0,1],[0,-1],[1,0],[-1,0]]
answer = 0
for i in c:
    temp_data = copy.deepcopy(data)
    temp_queue = copy.deepcopy(virus)
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in i:
        temp_data[j[0]][j[1]] = 1
    for j in temp_queue:
        visited[j[0]][j[1]] = True
    virus_zone = 0
    while temp_queue:
        y, x = temp_queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and temp_data[ny][nx] == 0:
                visited[ny][nx] = True
                temp_queue.append([ny, nx])
                virus_zone += 1
    answer = max(answer, (safe_count-3) - virus_zone)
print(answer)