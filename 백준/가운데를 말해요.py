import sys
import heapq

input = sys.stdin.readline
left, right = [], []
N = int(input())
data = []
for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    if right and left[0][1] > right[0][1]:
        left_max, right_min = heapq.heappop(left)[1], heapq.heappop(right)[1]
        heapq.heappush(left, (-right_min, right_min))
        heapq.heappush(right, (left_max, left_max))
    print(left[0][1])
