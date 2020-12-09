#https://www.acmicpc.net/problem/1937
# from itertools import product
# import sys
# from copy import deepcopy
# input = sys.stdin.readline
# n = int(input())
# bamboo= [[-sys.maxsize for i in range(n+1)]]
# for i in range(n):
#     bamboo.append([-sys.maxsize]+list(map(int, input().split()))+[-sys.maxsize])
# bamboo.append([-sys.maxsize for i in range(n+1)])
# bamboo_index = list(product(range(1,n+1), range(1,n+1)))
# d = [[1 for _ in range(n)] for _ in range(n)]
# direction = [(-1,0),(1,0),(0,-1),(0,1)]
# for x,y in bamboo_index:
#     p = [x,y]
#     bamboo_ = deepcopy(bamboo)
#     while p != []:
#         a = [(bamboo_[p[0]+i[0]][p[1]+i[1]],p[0]+i[0],p[1]+i[1]) for i in direction if bamboo_[p[0]][p[1]]<bamboo_[p[0]+i[0]][p[1]+i[1]]]
#         if a == []:
#             p = []
#             break
#         else:
#             a = sorted(a)[0]
#             p = [a[1],a[2]]
#             d[x-1][y-1] += 1
# ans = 0
# for s in d:
#     ans = max(ans, max(s))
# print(ans)
# --------------시간초과-------------------------------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(45000) #최대 재귀 깊이를 늘리기 #이런게 있었구나
direction = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(x, y):
    if data[x][y]: return data[x][y]
    else:
        data[x][y] = 1
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if bamboo[x][y] < bamboo[nx][ny]:
                    data[x][y] = max(data[x][y], dfs(nx, ny) + 1)
    return data[x][y]
n = int(input())
bamboo = [list(map(int, input().split())) for i in range(n)]
data = [[0] * n for i in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
print(result)