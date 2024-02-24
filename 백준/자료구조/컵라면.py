import heapq
import sys
cup = []
input = sys.stdin.readline
for i in range(int(input())):
    d, c = map(int,input().split())
    heapq.heappush(cup,(d, c))
answer = []
while cup:
    d, c = heapq.heappop(cup)
    heapq.heappush(answer, c)
    if d < len(answer):
        heapq.heappop(answer)
print(sum(answer))


