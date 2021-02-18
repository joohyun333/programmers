import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
data = [0]*1001
data[1],data[2] = 1,2
def DP(N):
    if N==1:
        return data[1]
    elif N == 2:
        return data[2]
    else:
        for i in range(3,N+1):
            data[i] = data[i-1]+data[i-2]
    return data[N]%10007
print(DP(int(input())))