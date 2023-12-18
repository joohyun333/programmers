# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

data = input().split()
N, M = int(data[0]), int(data[1])
maze = [[] for _ in range(N)]
discovered = [[False] * M for _ in range(N)]
for i in range(N):
    maze[i] = input()
answer = sys.maxsize
node = deque([(0, 0, 1)])
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while node:
    s = node.popleft()
    if s[0] == N-1 and s[1] == M-1:
        answer = min(answer, s[2])
    for i in direction:
        nextN, nextM = int(i[0] + s[0]), int(i[1] + s[1])
        if -1 < nextN < N and -1 < nextM < M and int(maze[nextN][nextM]) == 1 and discovered[nextN][nextM] == False:
            discovered[nextN][nextM] = True
            node.append((nextN, nextM, s[2]+1))

print(answer)