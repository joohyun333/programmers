import collections
import sys

input = sys.stdin.readline
N = int(input())
arr = collections.defaultdict(list)
for i in range(1, N + 1):
    index, *route, trash = map(int, input().split())
    for j, z in zip(route[::2], route[1::2]):
        arr[index].append((j, z))
def bfs(n):
    discoverd = [0] * (N + 1)
    queue = collections.deque([(n, 0)])
    discoverd[n] = True
    result, result_node = 0, 0
    while queue:
        node, dis = queue.popleft()
        if dis > result:
            result, result_node = dis, node
        for i, e in arr[node]:
            if not discoverd[i]:
                discoverd[i] = True
                queue.append((i, dis + e))
    return result, result_node
a, b= bfs(1)
print(bfs(b)[0])

