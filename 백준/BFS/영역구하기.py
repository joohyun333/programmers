# https://www.acmicpc.net/problem/2583
from collections import deque

data = input().split()
N, M, K = int(data[0]), int(data[1]), int(data[2])
area = [[False] * M for _ in range(N)]
for i in range(K):
    ban_area = input().split()
    for j in range(int(ban_area[1]), int(ban_area[3])):
        for z in range(int(ban_area[0]), int(ban_area[2])):
            area[j][z] = True

answer_count = 0
answer_size = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(idx):
    scope_size = 0
    node = deque(idx)
    while node:
        s = node.popleft()
        scope_size += 1
        for i in direction:
            nextN, nextM = int(i[0] + s[0]), int(i[1] + s[1])
            if -1 < nextN < N and -1 < nextM < M and not area[nextN][nextM]:
                node.append((nextN, nextM))
                area[nextN][nextM] = True
    return scope_size


for i in range(N):
    for j in range(M):
        if not area[i][j]:
            answer_count += 1
            area[i][j] = True
            size = bfs([(i, j)])
            answer_size.append(size)

print(answer_count)
for i in sorted(answer_size):
    print(i, end=" ")
