# https://www.acmicpc.net/problem/11722
from bisect import bisect_left
N = int(input())
data = list(map(int, input().split()))
list_ = [1]*N
for i in range(1,N):
    for j in reversed(range(i)):
        if data[i] < data[j] and list_[i] <= list_[j]:
            list_[i] = list_[j] + 1
print(max(list_))
