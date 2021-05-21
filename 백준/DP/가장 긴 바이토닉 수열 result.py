import sys
from builtins import list

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
re_arr = list(reversed(arr))
asc = [1] * N
desc = [1] * N
DP_arr = [[i] for i in arr]
re_DP_arr = [[i] for i in re_arr]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if asc[i] < asc[j] + 1:
                DP_arr[i] = DP_arr[j] + [arr[i]]
                asc[i] = asc[j] + 1
        if re_arr[i] > re_arr[j]:
            if desc[i] < desc[j] + 1:
                re_DP_arr[i] = re_DP_arr[j] + [re_arr[i]]
                desc[i] = desc[j] + 1
print(max([i + j for i, j in zip(asc, reversed(desc))])-1)
print(max([i + list(reversed(j))[1:] for i,j in zip(DP_arr, list(reversed(re_DP_arr)))], key=lambda a:len(a))
)