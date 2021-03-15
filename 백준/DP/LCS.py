# https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline
a = input()
b = input()
DP = [[0]*(len(a)) for _ in range(len(b))]
for i in range(1,len(b)):
    for j in range(1,len(a)):
        if b[i-1] == a[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
        else:
            DP[i][j] = max(DP[i - 1][j],DP[i][j-1])
for i in DP:
    print(i)
print(DP[len(b)-1][len(a)-1])