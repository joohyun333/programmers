import heapq
import sys


input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    p, d = map(int, input().split())
    heapq.heappush(data, [d, p])
answer = []
d_day = 1
while data:
    day, pay = heapq.heappop(data)
    if d_day >= day:
        if len(answer) < d_day:
            heapq.heappush(answer, pay)
        else:
            cheapest = heapq.heappop(answer)
            if cheapest < pay:
                heapq.heappush(answer, pay)
            else:
                heapq.heappush(answer, cheapest)
    d_day += 1
print(sum(answer))