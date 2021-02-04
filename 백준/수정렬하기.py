import sys
input = sys.stdin.readline
N = int(input())
a = [0]*10000
for i in range(N):
    b = int(input())
    a[b-1]+=1
for i, e in enumerate(a):
    for _ in range(e):
        print(i+1)