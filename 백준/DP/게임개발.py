import sys

input = sys.stdin.readline
N = int(input())
arr = [0] # [0, (1, 3), (2, 4), (3, 0), (4, 3)]
time = [0] * (N + 1)
for i in range(1, N + 1):
    m, *b, trash = map(int, input().split())
    if not b: arr.append((i, 0))
    for B in b:arr.append((i, B))
    time[i] = m
def DP(s):
    now_time, parent = s[0], s[1]
    if parent == 0:
        return time[now_time]
    return time[now_time]+DP(arr[parent])
result = [0]*(N+1)
for i in arr[1:]:
    m =  DP(i)
    if result[i[0]]<m:
        result[i[0]] = m
for i in result[1:]:
    print(i)


