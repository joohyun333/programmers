# https://www.acmicpc.net/problem/1325
from collections import deque
N, M = map(int, input().split())
parent = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    parent[b].append(a)
answers = {}
max_count = 0
for i in range(1, N+1):
    node = deque()
    node.append(i)
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    count = 0
    while node:
        count += 1
        n = node.popleft()
        if parent[n]:
            for j in parent[n]:
                if not visited[j]:
                    node.append(j)
                    visited[j] = True
    max_count = max(max_count, count)
    answers[i] = count
for i in sorted(answers):
    if answers[i] == max_count:
        print(i, end=" ")
