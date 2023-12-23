from collections import deque

M, N = map(int, input().split())
discovered = [[False for _ in range(M)] for _ in range(N)]
tomato_count = 0
ripe_tomato = deque()
for i in range(N):
    s = input().split()
    for j in range(M):
        if s[j] == '0':
            tomato_count += 1
        elif s[j] == '1':
            ripe_tomato.append([i, j, 0])
            discovered[i][j] = True
        else:
            discovered[i][j] = True
def bfs():
    q = ripe_tomato
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tomato_count = 0
    day = 0
    while q:
        y, x, z = q.popleft()
        day = z
        for i, j in direction:
            ny, nx = i + y, j + x
            if 0 <= ny < N and 0 <= nx < M and not discovered[ny][nx]:
                discovered[ny][nx] = True
                q.append((ny, nx, z+1))
                tomato_count -= 1
    return tomato_count, day


if tomato_count == 0:
    print(0)
else:
    ripe_tomato, day = bfs()
    result = tomato_count + ripe_tomato
    if result != 0:
        print(-1)
    else:
        print(day)
