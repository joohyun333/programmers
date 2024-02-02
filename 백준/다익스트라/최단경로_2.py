import heapq
from collections import defaultdict

V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
q = [[0, start]]
dis = [-1 for _ in range(V+1)]
while q:
    distance, point = heapq.heappop(q)
    if dis[point] == -1:
        dis[point] = distance
        for end, d in graph[point]:
            heapq.heappush(q, [distance + d, end])
for i in range(1, V+1):
    if dis[i] == -1:
        print("INF")
    else:
        print(dis[i])

