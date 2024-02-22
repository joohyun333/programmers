# https://www.acmicpc.net/problem/2792
N, M = map(int, input().split())
d = []
for i in range(M):
    d.append(int(input()))
start = 1
end = max(d)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in d:
        if i % mid == 0:
            count += i // mid
        else:
            count += (i // mid) + 1
    if count > N:
        start = mid + 1
    else:
        end = mid - 1
print(start)
