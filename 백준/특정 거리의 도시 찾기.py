# https://www.acmicpc.net/problem/18352
import collections
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
route = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    route[a].append(b)
discovered = [True] + [False] * N
queue = [(X, 0)]
result = []
while queue:
    v = queue.pop(0)
    print(v)
    if not discovered[v[0]]:
        discovered[v[0]] = True
        if v[1] == K:
            result.append(v[0])
        elif v[1]<K:
            for i in route[v[0]]:
                queue.append((i, v[1]+1))

if not result:
    print(-1)
else:
    for i in sorted(result):
        print(i)