# https://www.acmicpc.net/problem/16564
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
arr = [int(input()) for i in range(N)]
arr.sort()

start = 0
end = 1000000001
result = 0

while start <= end:
    mid = (start + end) // 2
    count = K
    for i in arr:
        if i < mid:
            count -= mid - i
    if count >= 0:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
