import sys
input = sys.stdin.readline
N = int(input())
s = set()
for i in range(N):
    s.add(input().rstrip("\n"))
s = list(s)
for i in sorted(s, key=lambda a: (len(a), ascii(a))):
    print(i)
