import sys, collections

input = sys.stdin.readline
N = int(input())
arr = collections.defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)



def find_depth(n):
    discoverd = [False] * (N + 1)
    depths = [0] * (N + 1)
    queue = [(n, 1)]
    discoverd[n] = True
    while queue:
        m, d = queue.pop()
        depths[m] = d
        for i in arr[m]:
            if not discoverd[i]:
                discoverd[i] = True
                queue.append((i, d + 1))
    return depths


dep_list = find_depth(1)


def find_euler_tour(a):
    queue = [a]
    while queue:
        if arr[a]:
            queue.append(a)
            a = arr[a].pop()
        else:
            route.append(a)
            a = queue.pop()
    return

route = []
depth = []
find_euler_tour(1)

for i in route:
    depth.append(dep_list[i])

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a_index, b_index = route.index(a, 1), route.index(b, 1)
    q, w = min(a_index, b_index), max(a_index, b_index)
    min_d, min_r = sys.maxsize, 0
    for d, r in zip(depth[q:w + 1], route[q:w + 1]):
        if d < min_d:
            min_d = d
            min_r = r
    print(min_r)
