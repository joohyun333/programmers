import sys

input = sys.stdin.readline
N = int(input())
d = list(map(int, input().split()))
lis = [-1000000001]
lis_idx = [0]


def binset(val):
    start = 0
    end = len(lis)
    while start < end:
        mid = (start + end) // 2
        if val > lis[mid]:
            start = mid + 1
        else:
            end = mid
    return start


for i in range(N):
    if lis[-1] < d[i]:
        lis.append(d[i])
        lis_idx.append(len(lis) - 1)
    else:
        s = binset(d[i])
        lis[s] = d[i]
        lis_idx.append(s)
lis_idx = lis_idx[1:]
a = max(lis_idx)
answer = []
temp = a
for i in range(len(lis_idx) - 1, -1, -1):
    if lis_idx[i] == temp:
        temp -= 1
        answer.append(str(d[i]))
print(a)
print(' '.join(answer[::-1]))
