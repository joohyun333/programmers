import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
start, end = 1, max(arr) * M
while start <= end:
    mid = (start + end) // 2
    person = sum([mid // i for i in arr])
    if person >= M:
        end = mid - 1
    elif person < M:
        start = mid + 1
print(start)
