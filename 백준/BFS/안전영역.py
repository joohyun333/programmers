import collections
import sys

input = sys.stdin.readline
arr = []
N = int(input())
for i in range(N):
    arr.append(list(map(int, input().split())))
rain = 0
maxium = max(sum(arr, []))
result = 0
go = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while rain <= maxium:
    data = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= rain:
                data[i][j] = 1

    queue = collections.deque()
    discoverd = [[False]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                queue.append((i, j))
                discoverd[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    data[x][y] = 0
                    for jx, jy in [(x + gx, y + gy) for gx, gy in go if 0 <= x + gx < N and 0 <= y + gy < N]:
                        if data[jx][jy] == 1 and not discoverd[jx][jy]:
                            discoverd[jx][jy] = True
                            queue.append((jx, jy))

                count+=1
    if result < count:
        result = count
    rain += 1
print(result)
