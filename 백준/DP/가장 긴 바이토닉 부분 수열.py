import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
re_arr = list(reversed(arr))
asc = [1] * N
desc = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            asc[i] = max(asc[i], asc[j] + 1)
        if re_arr[i] > re_arr[j]:
            desc[i] = max(desc[i], desc[j] + 1)
print(max([i + j for i, j in zip(asc, reversed(desc))])-1)
