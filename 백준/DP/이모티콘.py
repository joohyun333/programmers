# https://www.acmicpc.net/problem/14226
S = int(input())
DP = [0]*1001
DP[2] = 2
for i in range(3, 1002):
    DP[i] = min(DP[i-2]+2, )