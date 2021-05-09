# n,m = map(int, input().split())
# arr = [int(input()) for _ in range(n)]
# dp1 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)]
# dp2 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)]
# dp1[0][0] = 0
# dp2[0][1] = arr[0]
# for i in range(1, n):
#     dp1[i][0] = 0
#     dp2[i][0] = -float('inf')
#     for j in range(1,min(m, (i + 2) // 2) + 1):
#         dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
#         dp2[i][j] = max(dp1[i-1][j-1] + arr[i], dp2[i-1][j] + arr[i])
#
#
# print(max(dp1[n-1][m], dp2[n-1][m]))
N,M,*b=map(int,input().split())
a=[0]
exec('n=N and int(input());'
     'a,b=[*map(max,a+b[-1:],[0]+b)],[n+max(t)for t in zip(a,b+a[-1:])];'
     'print(a,b);'
     'N-=1;'*-~N)
# print(a[M])
# print(a, b )