# https://www.acmicpc.net/problem/1759
import heapq, sys

input = sys.stdin.readline
L, C = map(int, input().split())
arr = sorted(list(input().split()))
queue = []
consonant = ["a", "e", "i", "o", "u"]


def dfs(k, i, n, con, vow, discoverd):
    if n == L:
        if con >= 1 and vow >= 2:
            heapq.heappush(queue, k)
        return
    for j in range(i+1, C):
        d = discoverd[::]
        if not d[j]:
            d[j] = True
            if arr[j] in consonant:
                dfs(k + arr[j], j, n + 1, con + 1, vow, d)
            else:
                dfs(k + arr[j], j, n + 1, con, vow + 1, d)


discoverd = [False] * C
for i, e in enumerate(arr[:C - L + 1]):
    discoverd[i] = True
    if e in consonant:
        dfs(e, i, 1, 1, 0, discoverd)
    else:
        dfs(e, i, 1, 0, 1, discoverd)

while queue:
    print(heapq.heappop(queue))
