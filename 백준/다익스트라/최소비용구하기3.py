import heapq
from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)

for i in range(M):
	s,e,v = map(int, input().split())
	graph[s].append([e, v])
start, end = map(int, input().split())

distance = [-1 for _ in range(N+1)]
q = [[0, start]]
while q:
	d, p = heapq.heappop(q)
	if distance[p] == -1:
		distance[p] = d
		for pe, pd in graph[p]:
			heapq.heappush(q, [pd + d, pe])
print(distance[end])