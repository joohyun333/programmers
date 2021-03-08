# import sys
#
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# max_arr = sum(arr)
# DP = [[False] * (max_arr + 1) for _ in range(N)]
# result = [True] + [False] * (max_arr + 1)
# for i in range(N):
#     for j in range(max_arr + 1):
#         if j == 0:
#             DP[i][j] = True
#         elif i == 0:
#             DP[i][arr[0]] = True
#             result[arr[0]] =True
#         elif DP[i - 1][j]:
#             DP[i][j] = True
#             result[j] = True
#         elif 0 <= j - arr[i] < max_arr + 1 and DP[i - 1][j - arr[i]]:
#             DP[i][j] = True
#             result[j] = True
# DP.clear()
# for i in range(max_arr+2):
#     if not result[i]:
#         print(i)
#         break
#
import sys
input = sys.stdin.readline
N = int(input())
arr = tuple(map(int, input().split()))
DP = [[True]+[False]*sum(arr) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, sum(arr)+1):
        if arr[i-1] <= j :
            DP[i][j] = DP[i-1][j]|DP[i-1][j-arr[i-1]]
        else:
            DP[i][j] = DP[i-1][j]
for i,e in enumerate(DP[N]+[False]):
    if not e:
        print(i)
        break