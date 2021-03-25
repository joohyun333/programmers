# https://www.acmicpc.net/problem/11438
import sys, collections
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
log = 21
N = int(input())
arr = collections.defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(n, d):
    depth[n] = d
    for i in arr[n]:
        if not discoverd[i]:
            discoverd[n] = True
            parent[i][0] = n
            dfs(i, d + 1)

def set_parent():
    for i in range(1, log):
        for j in range(1, N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

discoverd = [True, True]+[False] * (N-1)
depth = [0] * (N + 1)
parent = [[0] * log for _ in range(N+1)]
dfs(1, 0)
set_parent()


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(log-1, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]
    if a == b:
        return a
    for i in range(log-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))


