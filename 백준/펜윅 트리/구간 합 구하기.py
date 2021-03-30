# https://www.acmicpc.net/problem/2042
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [0] * (N + 1)
tree = [0] * (N + 1)


def pre_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result


def update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)

def interval_sum(s, e):
    return  pre_sum(e) - pre_sum(s-1)

for i in range(1, N + 1):
    a = int(input())
    arr[i] = a
    update(i, a)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c-arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))
