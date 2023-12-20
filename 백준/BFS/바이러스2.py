# https://www.acmicpc.net/problem/2606
from collections import deque
def bfs():
    q = deque()
    q.append(1)
    discovered[1] = True
    count = 0
    while q:
        idx = q.popleft()
        count += 1
        for i in graph[idx]:
            if not discovered[i]:
                discovered[i] = True
                q.append(i)
    return count -1


com = int(input())
graph = [[] for _ in range(com + 1)]
discovered = [False for _ in range(com + 1)]
for i in range(int(input())):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

print(bfs())