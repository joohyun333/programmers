graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3],
}
from collections import deque
def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = deque()
    queue.append(start_v)
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
    return discoverd
print(iterative_bfs(1))
