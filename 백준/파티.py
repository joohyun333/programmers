import sys
import collections
import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())
route = collections.defaultdict(list)
for i in range(M):
    start, end, time = map(int, input().split())
    route[start].append([end, time])
min_time = [0] * N
X_list = []
rest_list = []
for i in range(1, N + 1):
    queue = [(0, i)]
    discoverd = [False] * (N + 1)
    min_time = [0] * (N + 1)
    while queue:
        time, node = heapq.heappop(queue)
        if not discoverd[node]:
            discoverd[node] = True
            min_time[node] = time
            for n_end, n_time in route[node]:
                heapq.heappush(queue, (time + n_time, n_end))
    rest_list.append(min_time[X])
    if i == X:
        X_list = min_time[1:]

result = 0
for r, x in zip(rest_list, X_list):
    if r+x > result:
        result = r+x
print(result)