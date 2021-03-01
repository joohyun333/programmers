N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))
stairs_dp = []
if len(stairs) < 3 :
    print(sum(stairs))
else:
    stairs_dp.append(stairs[0])
    stairs_dp.append(max(stairs[0]+stairs[1], stairs[1]))
    stairs_dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
    for i in range(3, N):
        temp  = max(stairs[i]+stairs[i-1]+stairs_dp[i-3], stairs[i]+stairs_dp[i-2])
        stairs_dp.append(temp)
    print(stairs_dp)