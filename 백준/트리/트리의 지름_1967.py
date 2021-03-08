import collections
import sys

input = sys.stdin.readline
N = int(input())
arr = collections.defaultdict(list)
for i in range(N - 1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))


def dfs(n):
    discoverd = [False] * (N + 1)
    discoverd[n] = True
    q = [(n, 0)]
    node, dis = 0, 0
    while q:
        n, d = q.pop()
        if d > dis:
            node, dis = n, d
        for i, e in arr[n]:
            if not discoverd[i]:
                discoverd[i] = True
                q.append((i, e + d))
    return node, dis

print(dfs(dfs(1)[0])[1])
