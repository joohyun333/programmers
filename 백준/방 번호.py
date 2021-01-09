# https://www.acmicpc.net/problem/1082
N = int(input())
value = list(map(int, input().split()))
dp = ['0']*(int(input())+1)
for i in range(N)[::-1]:
    c = value[i]
    for b in range(c, len(dp)):
        dp[b] = dp[b-c]+str(i) if int(dp[b]) <= int(dp[b-c]+str(i)) else dp[b]
    print(dp)
print(int(dp[-1]))