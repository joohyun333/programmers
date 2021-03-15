# https://www.acmicpc.net/problem/9252
import sys

input = sys.stdin.readline
a = input()
b = input()
DP = [[0] * (len(b)) for _ in range(len(a))]
DP_ = [[""] * (len(b)) for _ in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i - 1] == b[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
            DP_[i][j] += DP_[i - 1][j - 1] + a[i - 1]
        else:
            if DP[i - 1][j] > DP[i][j - 1]:
                DP[i][j] = DP[i - 1][j]
                DP_[i][j] += DP_[i - 1][j]
            else:
                DP[i][j] = DP[i][j - 1]
                DP_[i][j] += DP_[i][j - 1]
print(DP[len(a)-1][len(b)-1])
print(DP_[len(a)-1][len(b)-1])
