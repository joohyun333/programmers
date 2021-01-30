# https://www.acmicpc.net/problem/1431
import sys
import string
input = sys.stdin.readline
result = []
N = int(input())
for i in range(N):
    a = input().rstrip('\n')
    b = [len(a), 0, a]
    for j in a:
        if j in string.digits:
            b[1] += int(j)
    result.append(b)
for i in sorted(result):
    print(i[2])
