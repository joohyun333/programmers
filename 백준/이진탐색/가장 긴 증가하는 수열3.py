# https://www.acmicpc.net/problem/12015
import sys, bisect
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
result = [-1000000001]
for i in arr:
    if result[-1]<i:
        result.append(i)
    else:
        result[bisect.bisect_left(result,i)] = i
print(len(result)-1)
