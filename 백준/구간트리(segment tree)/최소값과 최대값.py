# https://www.acmicpc.net/problem/2357
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
total_binary = len(bin(N)) - 3
min_arr = []
max_arr = []
index = 2
while index <= 2 ** total_binary:
    a = []
    b = []
    for i in range(N - index + 1):
        a.append(min(min(arr[i:i+(index//2)]), min(arr[i+(index//2):i+index])))
        b.append(max(max(arr[i:i+(index//2)]), max(arr[i+(index//2):i+index])))
    min_arr.append(a)
    max_arr.append(b)
    index *= 2
for i in range(M):
    a, b = map(int, input().split())
    binary = len(bin(b - a + 1)) - 3
    c = min_arr[binary - 1]
    d = max_arr[binary - 1]
    min_num = min(c[a - 1], c[b - (2 ** binary)])
    max_num = max(d[a - 1], d[b - (2 ** binary)])
    print(min_num, max_num)