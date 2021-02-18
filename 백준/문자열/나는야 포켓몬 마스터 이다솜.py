import sys
import string
import collections
input = sys.stdin.readline
N, M = map(int, input().split())
arr = collections.defaultdict()
arr_e = collections.defaultdict()
for i in range(1,N+1):
    n = input().strip('\n')
    arr[i] = n
    arr_e[n] = i
problem = []
for i in range(M):
    problem.append(input())
for i in problem:
    if i[0] in string.digits:
        print(arr[int(i)])
    else:
        print(arr_e[i.strip('\n')])