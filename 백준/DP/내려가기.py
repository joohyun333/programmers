N = int(input())
arr = []
for i in range(N):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
DP_m = [0,0,0]
DP_s = [0,0,0]
for i in range(1, N + 1):
    m = [0,0,0]
    m[0] = arr[i - 1][0] + max(DP_m[0], DP_m[1])
    m[1] = arr[i - 1][1] + max(DP_m[0], DP_m[1], DP_m[2])
    m[2] = arr[i - 1][2] + max(DP_m[1], DP_m[2])
    DP_m=m

    s=[0,0,0]
    s[0] = arr[i - 1][0] + min(DP_s[0], DP_s[1])
    s[1] = arr[i - 1][1] + min(DP_s[0], DP_s[1], DP_s[2])
    s[2] = arr[i - 1][2] + min(DP_s[1], DP_s[2])
    DP_s = s
print(max(DP_m), min(DP_s))
