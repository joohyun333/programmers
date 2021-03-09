import sys, collections, heapq

input = sys.stdin.readline
N, E = map(int, input().split())
arr = collections.defaultdict(list)
for i in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
a, b = map(int, input().split())


def Dijkstra(s, e):
    discovered = [False] * (N + 1)
    queue = [(0, s)]
    while queue:
        dis, node = heapq.heappop(queue)
        if node == e:
            return dis
        if not discovered[node]:
            discovered[node] = True
            for i, d in arr[node]:
                heapq.heappush(queue, (dis + d, i))
    return -1


def search(route):
    if -1 in route:
        return -1
    else:
        return sum(route)


route1 = search([Dijkstra(1, a), Dijkstra(a, b), Dijkstra(b, N)])
route2 = search([Dijkstra(1, b), Dijkstra(b, a), Dijkstra(a, N)])
print(min(route1, route2))
