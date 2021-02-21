from collections import defaultdict, deque

N, M, V = map(int, input().split())
nodes = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[a].sort()
    nodes[b].append(a)
    nodes[b].sort()


def dfs(V, node=[]):
    check[V] = True
    print(V, end=' ')
    for i in nodes[V]:
        if not check[i]:
            dfs(i, node)


def bfs(V):
    queue = deque()
    queue.append(V)
    check[V] = True
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for i in nodes[n]:
            if not check[i]:
                check[i] = True
                queue.append(i)



check = [False] * (N + 1)
dfs(V)
print()
check = [False] * (N + 1)
bfs(V)
