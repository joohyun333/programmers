import sys
import collections
input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
d = collections.defaultdict()
for i,e in enumerate(sorted(set(data))):
    d[e] = i
for i in data:
    print(d[i], end=" ")
