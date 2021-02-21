from collections import deque
v, e = map(int, input().split()) #노드의 개수, 간선
indegree = [0]*(v+1) #진입차수
graph = [[]for i in range(v+1)] # 각노드에 연결된 간선정보

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1 #진입차수 증가

def topology_sort():
    result = [] # 알고리즘 수행결과
    q = deque() # 처음 시작할때 진입차수 0노드를 큐에 삽입
    for i in range(1, v+1):
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

