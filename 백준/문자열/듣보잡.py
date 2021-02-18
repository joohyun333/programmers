import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n, m =set(),set()
for i in range(N):
    n.add(input())
for i in range(M):
    m.add(input())
p = n&m
print(len(p))
for i in sorted(p):
    print(i)
