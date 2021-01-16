# https://www.acmicpc.net/problem/2606
import collections
com = int(input())
link_num = int(input())
link = collections.defaultdict(list)
for i in range(link_num):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
def search(graph, n):
    queue = [n]
    discovered = []
    while queue:
        v = queue.pop(0)
        if v not in discovered:
            discovered.append(v)
            print(discovered)
            for i in graph[v]:
                if i not in discovered and i not in queue:
                    queue.append(i)
    return len(discovered)-1
print(search(link, 1))
