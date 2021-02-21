from collections import deque
N, M = map(int, input().split())
indegree = [0]*(N+1) #진입차수
graph = [[]for i in range(N+1)] # 각노드에 연결된 간선정보
for i in range(M):
    a, b =map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = [] # 알고리즘 수행결과
    q = deque() # 처음 시작할때 진입차수 0노드를 큐에 삽입
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
    for i in result:
        print(i, end=" ")
topology_sort()
