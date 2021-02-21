import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)
result = []
for i in arr:
    num = abs(i)
    if num > 0 :
        heapq.heappush(result, (num, i))
    else:
        if result:
            m = heapq.heappop(result)
            print(m[1])
        else:
            print(0)