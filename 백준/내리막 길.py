# https://www.acmicpc.net/problem/1520
import sys

input = sys.stdin.readline
M, N = map(int, input().split())
route = []
for i in range(M):
    route.append(list(map(int, input().split())))
def dfs(x, y, count=0):
    before_x, before_y = 0, 0
    print(x, y)
    discoverd = [[[False] for _ in range(N)] for _ in range(M)]
    if x < 0 or x > N or y < 0 or y > M:
        return
    elif x == N - 1 and y == M - 1:
        return True
    elif not discoverd[x][y] and route[before_x][before_y] <= route[x][y])::
        discoverd[x][y] = True
        dfs(x - 1, y, count)
        dfs(x + 1, y, count)
        dfs(x, y - 1, count)
        dfs(x, y + 1, count)
    before_x, before_y = x, y
    return count
print(dfs(0, 0))
