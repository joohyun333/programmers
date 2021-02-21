from collections import deque
N = int(input())
indegree = [0]*(N+1) #진입차수
graph = [[]for i in range(N+1)] # 각노드에 연결된 간선정보
point = [0]
for i in range(1,N+1):
    p, *node, trash = map(int, input().split())
    for j in node:
        graph[i].append(j)
        indegree[j] += 1
    point.append(p)

def topology_sort():
    q = deque()
    result = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)
    return result[::-1]
a = topology_sort()
answer = [0] *(N+1)
for i in a:
    if not graph[i]:
        answer[i] = point[i]
    else:
        for j in graph[i]:
            answer[i] = max(answer[i], answer[j]+point[i])
for i in answer[1:]:
    print(i)