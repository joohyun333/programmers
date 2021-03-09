# https://www.acmicpc.net/problem/1389
import collections
import sys
N, M = map(int, input().split())
friends = collections.defaultdict(list)
for i in range(M):
    a, b =list(map(int, input().split()))
    friends[a].append(b)
    friends[b].append(a)
def bfs(s):
    count_memory = [0]*(N+1)
    # print(count_memory)
    discovered = []
    queue = [(s,0)]
    while queue:
        v = queue.pop(0)
        if v[0] not in discovered:
            discovered.append(v[0])
            count_memory[v[0]]+=v[1]
            print(count_memory)
            for i in friends[v[0]]:
                queue.append((i,v[1]+1))
                print(queue)
    return sum(count_memory)
min, index = sys.maxsize, 0
for i in range(1, N+1):
    amount = bfs(i)
    if amount < min:
        min = amount
        index = i
print(index)

