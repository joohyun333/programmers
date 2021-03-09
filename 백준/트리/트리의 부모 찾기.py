import collections, sys
input = sys.stdin.readline
N = int(input())
arr = collections.defaultdict(list)
for i in range(N-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
result = [0]*(N+1)
def bfs(a):
    discoverd = [False]*(N+1)
    queue = collections.deque([a])
    while queue:
        v = queue.pop()
        discoverd[v] = True
        for i in arr[v]:
            if not discoverd[i]:
                result[i] = v
                queue.append(i)
    return
bfs(1)
for i in range(2, N+1):
    print(result[i])