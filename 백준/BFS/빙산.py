import collections
import sys
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
go = [(-1, 0), (1, 0), (0, -1), (0, 1)]
year = 0
while True:
    discoverd = [[False] * M for _ in range(N)]
    memory = copy.deepcopy(arr)
    queue = collections.deque()
    ice = []
    zero = []
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not discoverd[i][j]:
                discoverd[i][j] = True
                count += 1
                queue.append((i, j))
                while queue:
                    gi, gy = queue.popleft()
                    cnt = 0
                    for a, b in [(gi + x, gy + y) for x, y in go if 0 <= gi + x < N and 0 <= gy + y < M]:
                        if not discoverd[a][b]:
                            if arr[a][b] != 0:
                                discoverd[a][b] = True
                                queue.append((a, b))
                            elif arr[a][b] == 0:
                                cnt += 1
                    zero.append((gi, gy, cnt))
    for i, j, c in zero:
        if arr[i][j] >= c:
            arr[i][j] = arr[i][j] - c
        else:
            arr[i][j] = 0
    if count >= 2:
        print(year)
        break
    elif count == 0:
        print(0)
        break
    year += 1
