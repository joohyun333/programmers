# https://www.acmicpc.net/problem/1753
from collections import defaultdict
import heapq
V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
for i in range(E):
    a, b, c  = map(int, input().split())
    graph[a].append((b, c))
route = [(0, K)]
dist = defaultdict(int)
print(graph)
while route:
    print(route)
    time, node = heapq.heappop(route)
    if node not in dist:
        dist[node] = time
        for i, t in graph[node]:
            alt = time+t
            heapq.heappush(route, (alt, i))
for i in range(1, V+1):
    if i in dist:
        print(dist[i])
    else :
        print("INF")