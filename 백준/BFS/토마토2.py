from collections import deque

M, N = map(int, input().split())
discovered = [[False for _ in range(M)] for _ in range(N)]
tomato_count = 0
for i in range(N):
    s = input().split()
    for j in range(M):
        if s[j] == '0':
            tomato_count += 1


def bfs():
    q = deque((N - 1, M - 1))
    discovered[N - 1][M - 1] = True
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tomato_count = 0
    while q:
        y, x = q.popleft()
        for i, j in direction:
            ny, nx = i + y, j + x
            if 0 <= ny < N and 0 <= nx < M and not discovered[ny][nx]:
                discovered[ny][nx] = True
                q.append((ny, nx))
                tomato_count -= 1
    return tomato_count


if tomato_count == 0:
    print(0)
else:
    result = tomato_count + bfs()
    if (tomato_count == result):
        print(-1)
    else:
        print(result)
