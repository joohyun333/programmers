# https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()
DP = [[0]*(len(a)+1) for _ in range(len(b)+1)]
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if b[i-1] == a[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
        else:
            DP[i][j] = max(DP[i - 1][j],DP[i][j-1])
print(DP[len(b)][len(a)])