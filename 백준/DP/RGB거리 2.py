# https://www.acmicpc.net/problem/17404
import sys, copy
input = sys.stdin.readline
N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))
DP_1 = copy.deepcopy(RGB)
DP_1[0][0] = 1001
DP_1[0][1] = 1001

DP_2 = copy.deepcopy(RGB)
DP_2[0][0] = 1001
DP_2[0][2] = 1001

DP_3 = copy.deepcopy(RGB)
DP_3[0][1] = 1001
DP_3[0][2] = 1001

def DP_solution(data, first):
    for i in range(1,N):
        data[i][0] = min(data[i][0]+data[i - 1][1], data[i][0]+data[i - 1][2])
        data[i][1] = min(data[i][1]+data[i - 1][0], data[i][1]+data[i - 1][2])
        data[i][2] = min(data[i][2]+data[i - 1][0], data[i][2]+data[i - 1][1])

    n = data[N - 1].index(min(data[N - 1]))
    if n != first:
        return min(data[N-1])
    else:
        return sorted(data[N-1])[1]

answer = []
answer.append(DP_solution(DP_1, 2))
answer.append(DP_solution(DP_2, 1))
answer.append(DP_solution(DP_3, 0))
print(min(answer))