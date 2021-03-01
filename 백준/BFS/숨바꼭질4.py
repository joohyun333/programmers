import collections

start, end = map(int, input().split())
queue = collections.deque([start])
discoverd = [0] * 100001
route = [0] * 100001
go = ["-1", "+1", "*2"]
while queue:
    q = queue.popleft()
    if q == end:
        arr = []
        a = q
        for _ in range(discoverd[q]+1):
            arr.append(a)
            a = route[a]
        break
    for j in go:
        m = eval(str(q) + j)
        if 0 <= m <= 100000 and discoverd[m]==0:
            discoverd[m] = discoverd[q]+1
            route[m] = q
            queue.append(m)
print(len(arr)-1)
print(' '.join(map(str, arr[::-1])))