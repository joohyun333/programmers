# https://www.acmicpc.net/problem/11505
import math, sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
h = int(math.ceil(math.log2(n)))
tree = [0] * (1 << (h + 1))


def update(n, start, end, idx, val):
    if idx < start or end < idx:
        return
    if start == end:
        tree[n] = val
        return

    mid = (start + end) // 2
    update(n * 2, start, mid, idx, val)
    update(n * 2 + 1, mid + 1, end, idx, val)
    tree[n] = (tree[n * 2] * tree[n * 2 + 1]) % 1000000007


def pre_Mul(node, start, end, left, right):
    if start > right or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    reault = pre_Mul(node * 2, start, mid, left, right) * pre_Mul(node * 2 + 1, mid + 1, end, left, right) % 1000000007
    return reault


arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
    update(1, 0, n - 1, i, num)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
        update(1, 0, n - 1, b - 1, c)
    else:
        print(pre_Mul(1, 0, n - 1, b - 1, c - 1))
