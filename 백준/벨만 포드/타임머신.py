# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
dist = [sys.maxsize] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))


def bf():
    dist[1] = 0
    for i in range(N):
        for j in range(M):
            start = arr[j][0]
            end = arr[j][1]
            worth = arr[j][2]
            if dist[start] != sys.maxsize and dist[end]>dist[start]+worth:
                dist[end] = dist[start] + worth
                if i == N - 1:
                    return True
    return False


minus_cycle = bf()
if minus_cycle:
    print(-1)
else:
    for i in dist[2:]:
        if i == sys.maxsize:
            print(-1)
        else:
            print(i)
