N = int(input())
drink = []
for i in range(N):
    drink.append(int(input()))
DP = [0]*(N)
for i in range(N):
    if i == 0:
        DP[i] = drink[0]
    elif i ==1:
        DP[i] = drink[0]+drink[1]
    elif i == 2:
        DP[i] = max(DP[1], drink[0]+drink[2], drink[1]+drink[2])
    else:
        DP[i]  = max(drink[i]+drink[i-1]+DP[i-3], drink[i]+DP[i-2], DP[i-1])
print(DP[N-1])