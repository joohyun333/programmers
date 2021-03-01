import heapq
import collections

start, end = map(int, input().split())
queue = [(0, start)]
discoverd = [False] * 100001
while queue:
    time, node = heapq.heappop(queue)
    if 0 <= node <= 100000 and not discoverd[node]:
        discoverd[node] = True
        if node == end:
            print(time)
            break
        heapq.heappush(queue, [time+1, node - 1])
        heapq.heappush(queue, [time+1, node + 1])
        heapq.heappush(queue, [time, node * 2])

