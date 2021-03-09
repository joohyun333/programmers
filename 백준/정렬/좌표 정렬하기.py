import sys
input = sys.stdin.readline
N = int(input())
s = []
for i in range(N):
    a, b = map(int, input().split())
    s.append([a,b])
s = sorted(s, key=lambda a:(a[0], a[1]))
for i, j in s:
    print(i, j)