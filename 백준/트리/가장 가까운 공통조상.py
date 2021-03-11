# https://www.acmicpc.net/problem/3584
import sys, collections
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n = int(input())
    arr = collections.defaultdict(list)
    parent = [i for i in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        arr[a].append(b)
        parent[b] = a
    node_1, node_2 = map(int, input().split())
    p = [i for i, e in enumerate(parent) if i > 0 and i == e]


    def bfs(p, goal):
        queue = collections.deque()
        queue.append([p, [p]])
        discoverd = [False] * (n + 1)
        while queue:
            m, r = queue.popleft()
            if not discoverd[m]:
                discoverd[m] = True
                if m == goal:
                    return r
                for i in arr[m]:
                    queue.append([i, r + [i]])

    for i in p:
        a = bfs(i, node_1)
        b = bfs(i, node_2)
        result = 0
        for aa, bb in zip(a,b):
            if aa==bb:
                result = aa
    print(result)

