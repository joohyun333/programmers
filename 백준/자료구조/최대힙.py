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
    if i > 0 :
        heapq.heappush(result, -i)
    else:
        if result:
            m = heapq.heappop(result)
            print(-m)
        else:
            print(0)