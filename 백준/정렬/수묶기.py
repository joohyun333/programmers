import sys
import functools
input = sys.stdin.readline
N = int(input())
arr = []
result = 0
for i in range(N):
    arr.append(int(input()))
if N > 2:
    arr.sort()
    *a, b, c = arr
    num1 = sum(a) + (b * c)
    a, b, *c = arr
    num2 = sum(c) + (a * b)
    print(max(sum(arr), num1, num2))
else:
    print(functools.reduce(lambda a,b: a*b,arr))