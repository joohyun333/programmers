import sys

input = sys.stdin.readline
N = int(input())
num = [0 for _ in range(N+1)]
for i in range(2, N + 1):
    num[i] = num[i-1]+1
    if i % 2 == 0:
        num[i] = min(num[i // 2]+1, num[i])
    if i % 3 == 0:
        num[i] = min(num[i // 3]+1, num[i])
print(num[N])
