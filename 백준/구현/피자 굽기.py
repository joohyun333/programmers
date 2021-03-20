import sys, collections

input = sys.stdin.readline
D, N = map(int, input().split())
arr = list(map(int, input().split()))
dough = collections.deque(map(int, input().split()))
possibe_arr = []
min_arr = sys.maxsize
for i in range(D):
    min_arr = min(min_arr, arr[i])
    possibe_arr.append(min_arr)

floor = D - 1
highest_floor = 0
d = dough.popleft()
while floor > -1:
    if possibe_arr[floor] >= d:
        highest_floor = floor
        if floor > 0 and dough:
            d = dough.popleft()
        else:
            break
    floor -= 1

if dough or highest_floor == 0:
    print(0)
else:
    print(highest_floor+1)
