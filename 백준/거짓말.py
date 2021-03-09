import sys, collections

input = sys.stdin.readline
N, M = map(int, input().split())
lie_num, *lier = map(int, input().split())
arr = collections.defaultdict(set)
p = []
for i in range(M):
    party_num, *party = map(int, input().split())
    for j in range(party_num):
        for z in range(party_num):
            arr[party[j]].add(party[z])
    p.append(party)
lie = [1] + [0] * N


def dfs(n):
    lie[n] = 1
    for i in arr[n]:
        if not lie[i]:
            lie[i] = 1
            dfs(i)
    return


for i in lier:
    dfs(i)
arr.clear()

count = 0
for i in p:
    b = True
    for j in i:
        if lie[j]:
            b = False
            break
    if b: count += 1
print(count)
