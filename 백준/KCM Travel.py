import collections
import heapq
import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    route = collections.defaultdict(list)
    N, M, K = map(int, input().split())
    discovered = [False] * (N + 1)
    for i in range(K):
        u, v, c, d = map(int, input().split())  # 출발, 도착, 비용, 소요시간
        route[u].append((v, c, d))
    queue = [(0, 0, 1)]  # 소요시간(d), 비용(c), 도착(v)
    while queue:
        print(queue)
        time, cost, dis = heapq.heappop(queue)
        if dis == N:
            print(time)
            break
        for v, c, d in route[dis]:
            if M>=cost+c:
                heapq.heappush(queue, (time+d, cost+c, v))
    if not queue:
        print("Poor KCM")