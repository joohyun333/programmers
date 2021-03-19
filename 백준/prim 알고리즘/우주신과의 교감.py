# https://www.acmicpc.net/problem/1774
import heapq, math, sys

input = sys.stdin.readline
N, M = map(int, input().split())
p = [[0]]
link = []
parent = [i for i in range(N + 1)]
size = [1 for i in range(N + 1)]
for _ in range(N):
    p.append(list(map(int, input().split())))
for _ in range(M):
    link.append(list(map(int, input().split())))


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def unite(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        if size[a_parent] >= size[b_parent]:
            size[a_parent] += size[b_parent]
            parent[b_parent] = a_parent
            for i in range(1,N+1):
                if parent[i] == b_parent:
                    parent[i] = a_parent
        else:
            size[b_parent] += size[a_parent]
            parent[a_parent] = b_parent
            for i in range(1,N+1):
                if parent[i] == a_parent:
                    parent[i] = b_parent

for node1, node2 in link:
    unite(node1, node2)
link.clear()

queue = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and parent[i] != parent[j]:
            dis = math.sqrt(((p[i][0] - p[j][0]) ** 2) + ((p[i][1] - p[j][1]) ** 2))
            heapq.heappush(queue, (dis, i, j))
p.clear()

total_dis = 0
while queue:
    dis, a, b = heapq.heappop(queue)
    if parent[a] != parent[b]:
        unite(a, b)
        total_dis += dis
print("%.2f" % total_dis)
