import sys

input = sys.stdin.readline
num = []
N, M = map(int, input().split())
for i in range(N):
    num.append(int(input()))
num.sort()
start = end = 0
min_result = sys.maxsize
while end<N and start <= end:
    distance = num[end] - num[start]
    if distance >=M :
        if min_result> distance:
            min_result = distance
        start+=1
    else:
        end+=1
print(min_result)