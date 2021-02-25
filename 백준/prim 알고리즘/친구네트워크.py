import sys
import collections


def search_parent(parent, n):
    if parent[n] != n:
        parent[n] = search_parent(parent, parent[n])
    return parent[n]


def union_parent(parent, answer, a, b):
    x = search_parent(parent, a)
    y = search_parent(parent, b)
    if x != y:
        answer[x] = answer[x].union(answer[y])
        parent[y] = x
        answer[x].add(a)
        answer[x].add(b)
        answer[y].clear()


N = int(input())
input = sys.stdin.readline
for _ in range(N):
    parent = collections.defaultdict(list)
    answer = collections.defaultdict(set)
    link = collections.deque()
    n = int(input())
    for _ in range(n):
        a, b = map(str, input().split())
        if not parent[a]:
            parent[a] = a
        if not parent[b]:
            parent[b] = b
        union_parent(parent, answer, a, b)
        print(len(answer[parent[a]]))
