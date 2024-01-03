# https://www.acmicpc.net/problem/2234
from collections import deque

N, M = map(int, input().split())
maze = [['' for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 남동북서
for i in range(M):
    data = list(map(int, input().split()))
    for j in range(N):
        maze[i][j] = str(bin(data[j])).replace('0b', '').zfill(4)


def bfs(m, n, group_num):
    dq = deque()
    dq.append((m, n))
    group_size = 0
    while dq:
        y, x = dq.popleft()
        group_map[y][x] = group_num
        bit_direction = maze[y][x]
        group_size += 1
        for idx, direct in enumerate(bit_direction):
            if direct == '0':
                ny, nx = y + direction[idx][0], x + direction[idx][1]
                if -1 < ny < M and -1 < nx < N and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((ny, nx))
    return group_size


group = 0
widest_size = 0
sum_widest_size = 0
group_map = [[0 for _ in range(N)] for _ in range(M)]
group_size_list = {}
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            group += 1
            result = bfs(i, j, group)
            widest_size = max(widest_size, result)
            group_size_list[group] = result


def group_bfs(i, j, group_num):
    dq = deque()
    dq.append((i, j))
    close_list = set()
    sum_widest_in_group_num = 0
    while dq:
        y, x = dq.popleft()
        for direct in direction:
            ny, nx = y + direct[0], x + direct[1]
            if -1 < ny < M and -1 < nx < N:
                if group_map[ny][nx] != group_num:
                    close_list.add(group_map[ny][nx])
                if not visited[ny][nx] and group_map[ny][nx] == group_num:
                    visited[ny][nx] = True
                    dq.append((ny, nx))
    for i in close_list:
        sum_widest_in_group_num = max(sum_widest_in_group_num, group_size_list[group_num] + group_size_list[i])
    return sum_widest_in_group_num


close_group = {}
visited = [[False for _ in range(N)] for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            sum_widest_in_group = group_bfs(i, j, group_map[i][j])
            sum_widest_size = max(sum_widest_size, sum_widest_in_group)

print(group)
print(widest_size)
print(sum_widest_size)
