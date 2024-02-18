# https://www.acmicpc.net/problem/1987
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = {(0, 0, graph[0][0])}

answer = 1
while q:
    y, x, route = q.pop()
    answer = max(answer, len(route))
    for dy, dx in direction:
        ny, nx = dy + y, dx + x
        if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] not in route:
            q.add((ny, nx, route+graph[ny][nx]))
print(answer)