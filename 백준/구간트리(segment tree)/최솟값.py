# https://www.acmicpc.net/problem/10868
import math, sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
h = int(math.ceil(math.log2(n)))
min_tree = [0] * (1 << (h + 1))

def init_min(n, start, end):
    if start == end:
        min_tree[n] = arr[start]
        return min_tree[n]
    mid = (start+end)//2
    min_tree[n] = min(init_min(n*2, start, mid), init_min((n*2)+1, mid+1, end))
    return min_tree[n]

def queryMin(node, start, end, left, right):
    if start > right or end <left:
        return sys.maxsize
    if left <= start and end <= right :
        return min_tree[node]
    mid = (start+end)//2
    return min(queryMin(node*2, start, mid, left, right), queryMin((node*2)+1, mid+1, end, left, right))

init_min(1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
    print(queryMin(1, 0, n-1, a-1, b-1))