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
queue = [(0, start,[start])]
while queue:
    dis, node, route= heapq.heappop(queue)
    if node == end:
        print(dis)
        print(len(route))
        print(' '.join(map(str,route)))
        break
    if not discoverd[node]:
        discoverd[node] = True
        for i, e in arr[node]:
            heapq.heappush(queue, (dis + e, i, route+[i]))
