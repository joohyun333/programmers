N = int(input())
d = list(map(int, input().split()))
lis = [-1000000001]

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
    else:
        s = binset(d[i])
        lis[s] = d[i]
print(len(lis)-1)