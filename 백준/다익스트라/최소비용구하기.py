import sys, collections, heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
arr = collections.defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
start, end = map(int, input().split())
discoverd = [False] * (N + 1)
queue = [(0, start)]
while queue:
    dis, node = heapq.heappop(queue)
    if node == end:
        print(dis)
        break
    if not discoverd[node]:
        discoverd[node] = True
        for i, e in arr[node]:
            heapq.heappush(queue, (dis + e, i))
