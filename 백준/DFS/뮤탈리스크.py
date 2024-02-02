import sys
from itertools import permutations

N = int(input())
scv = list(map(int, input().split()))
mu = [9, 3, 1]
case = list(permutations(mu[:N], N))
visited = {}
answer = sys.maxsize


def dfs(s, atk_count):
    global answer
    for i in range(len(case)):
        next_s = []
        for sval, cval in zip(s, case[i]):
            result = sval - cval if sval - cval > 0 else 0
            next_s.append(result)
        if next_s.count(0) == len(next_s):
            answer = min(answer, atk_count)
        else:
            k = ''
            for j in range(N):
                k += format(next_s[j], '02')
            if not visited.get(k):
                visited[k] = atk_count
                dfs(next_s, atk_count + 1)
            else:
                if visited.get(k) > atk_count:
                    visited[k] = atk_count
                    dfs(next_s, atk_count + 1)



if scv.count(0) == len(scv):
    print(0)
else:
    dfs(scv, 1)
    print(answer)