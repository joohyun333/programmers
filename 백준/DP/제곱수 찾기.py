# https://www.acmicpc.net/problem/1025
import itertools, math, sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [input().strip() for i in range(N)]
result = -1

for n, m in itertools.product(range(N), range(M)):
    for interval_n in range(-N, N):
        for interval_m in range(-M, M):
            if interval_m == 0 and interval_n == 0:
                continue
            y, x = n, m
            turn = 1
            num = ''
            while 0 <= y < N and 0 <= x < M:
                num += arr[y][x]
                sqrt_num = math.sqrt(int(num))
                if sqrt_num.is_integer():
                    result = max(result, int(num))
                y = n + (turn * interval_n)
                x = m + (turn * interval_m)
                turn += 1
print(result)
