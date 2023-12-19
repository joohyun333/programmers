# https://www.acmicpc.net/problem/2644

def dfs(node, target, answer):
    if not discovered[node]:
        discovered[node] = True
        if down_graph[node]:
            for i in down_graph[node]:
                if i == target:
                    return answer + 1
                else:
                    dfs(i, target, answer + 1)
        if up_graph[node]:
            if up_graph[node] == target:
                return answer + 1
            else:
                return dfs(up_graph[node], target, answer + 1)
    return None

N = int(input())
target_1, target_2 = map(int, input().split())
root = set([i for i in range(1, N+1)])
down_graph = [[] for _ in range(N + 1)]
up_graph = [0 for _ in range(N + 1)]
global discovered
for _ in range(int(input())):
    t1, t2 = map(int, input().split())
    down_graph[t1].append(t2)
    up_graph[t2] = t1
    if t2 in root:
        root.remove(t2)
discovered = [False for _ in range(N+1)]
result = dfs(target_1, target_2, 0)
if result is None:
    result = -1
print(result)





