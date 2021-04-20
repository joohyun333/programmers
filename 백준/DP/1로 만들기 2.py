# https://www.acmicpc.net/problem/12852
import sys, collections
dic = collections.defaultdict(str)
input = sys.stdin.readline
N = int(input())
num = [0 for _ in range(N + 1)]
arrs = [i for i in range(N + 1)]
for i in range(2, N + 1):
    num[i] = num[i - 1] + 1
    arrs[i] = i - 1
    if i % 2 == 0:
        if num[i] > num[i // 2] + 1:
            num[i] = num[i // 2] + 1
            arrs[i] = i // 2
    if i % 3 == 0:
        if num[i] > num[i // 3] + 1:
            num[i] = num[i // 3] + 1
            arrs[i] = i // 3
print(num[N])
result = []


def dfs(n):
    if n == 1:
        result.append(1)
        return
    result.append(n)
    dfs(arrs[n])


dfs(N)
print(' '.join(map(str, result)))