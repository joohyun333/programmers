import sys
import heapq
# input = sys.stdin.readline
N, M =map(int, input().split())
route = []
discoverd = [False]*(N+1)
for _ in range(M):
    a,b,c = map(int, input().split())
    route.append((c,a,b))
parent = [i for i in range(N+1)]

def search_parent(parent, n):
    if parent[n] != n:
        parent[n] = search_parent(parent, parent[n])
    return parent[n]

def union_parent(parent,a,b):
    x = search_parent(parent, a)
    y = search_parent(parent, b)
    if x<y:
        parent[y] = x
    else:parent[x] = y

heapq.heapify(route)
result = []
while route:
    time, start, end = heapq.heappop(route)
    if search_parent(parent, start) != search_parent(parent, end):
        union_parent(parent, start, end)
        result.append(time)
result.sort()
print(sum(result[:-1]))