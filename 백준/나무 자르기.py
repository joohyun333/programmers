# https://www.acmicpc.net/problem/2805
from typing import List
N, K = map(int,input().split())
woods: List[int] = sorted(list(map(int, input().split())))
min_num, max_num = 0, max(woods)
while min_num < max_num:
    mid: int = (max_num + min_num)//2
    total: int = sum([i-mid for i in woods if mid<i])
    if total > K and min_num != mid:
        min_num = mid
    elif total < K and max_num != mid:
        max_num = mid
    else:
        break
print(mid)


