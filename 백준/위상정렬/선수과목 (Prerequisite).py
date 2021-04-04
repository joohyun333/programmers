# https://www.acmicpc.net/problem/14567
import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
semester = [1] * (N + 1)
indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    indegree[a] += 1

queue = collections.deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

p = []
while queue:
    q = queue.popleft()
    p.append(q)
    for i in graph[q]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

for i in p[::-1]:
    for j in graph[i]:
        semester[i] = max(semester[i],semester[j] + 1)
print(' '.join(map(str, semester[1:])))
