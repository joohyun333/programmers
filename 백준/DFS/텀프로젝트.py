# https://www.acmicpc.net/problem/1005
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    arr = [0]+list(map(int, input().split()))

    def dfs(n):
        global result
        discoverd[n]=True
        go.append(n)
        a = arr[n]
        if discoverd[a]:
            if a in go:
                result+=go[go.index(a):]
            return
        else:
            dfs(a)

    discoverd = [True]+[False]*N
    result = []
    for i, e in enumerate(arr):
        if not discoverd[i]:
            go = []
            dfs(i)
    print(N-len(result))
