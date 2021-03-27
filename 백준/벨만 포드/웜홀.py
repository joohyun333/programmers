# https://www.acmicpc.net/problem/1865
import sys, collections

input = sys.stdin.readline
arr = collections.defaultdict(list)
for _ in range(int(input())):
    arr = set()
    N, M, W = map(int, input().split())
    cost = [[10001] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        S, E, T = map(int, input().split())
        cost[S][E] = min(cost[S][E], T)
        cost[E][S] = min(cost[E][S], T)
        arr.add((S, E))
        arr.add((E, S))
    for i in range(W):
        S, E, T = map(int, input().split())
        cost[S][E] = min(cost[S][E], -T)
        arr.add((S, E))
    arr = list(arr)
    result = "NO"
    dist = [sys.maxsize] * (N + 1)
    for i in range(N):
        for j in range(len(arr)):
            a = arr[j][0]
            b = arr[j][1]
            c = cost[a][b]
            if dist[b]> dist[a]+c:
                dist[b] = dist[a]+c
                if i == N-1:
                    result = "YES"
    print(result)