import sys
import heapq
import math

input = sys.stdin.readline
N = int(input())
route = []
for _ in range(N):
    x, y = map(float, input().split())
    route.append((x, y))
parent = [i for i in range(N + 1)]
routes = []
for i in range(len(route)):
    for j in range(i + 1, len(route)):
        routes.append((math.sqrt((route[i][0] - route[j][0]) ** 2 + (route[i][1] - route[j][1]) ** 2), i, j))
route.clear()
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

heapq.heapify(routes)
result =0
while routes:
    time, start, end = heapq.heappop(routes)
    if search_parent(parent, start) != search_parent(parent, end):
        union_parent(parent, start, end)
        result+=time
print(result)
