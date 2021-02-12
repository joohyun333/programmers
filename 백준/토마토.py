import collections
M, N = map(int, input().split()) # M 가로 # N 세로
tomato_ripe = []
box = []
for i in range(N):
    m = list(map(int, input().split()))
    box.append(m)
    for j in range(M):
        if box[i][j] == 1:
            tomato_ripe.append((i, j))

def bfs(node):
    queue = collections.deque()
    for nodes in node:
        queue.append((nodes, 0))
    while queue:
        q = queue.popleft()
        n, count = q[0], q[1]
        s = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        route = [(n[0] + i[0], n[1] + i[1]) for i in s if 0 <= n[0] + i[0] < N and 0 <= n[1] + i[1] < M]
        for row, col in route:
            tomato = box[row][col]
            if tomato == 0:
                queue.append(((row, col), count+1))
                box[row][col] = 1
    for n in range(N):
        if 0 in box[n]:
            return -1
    return count
print(bfs(tomato_ripe))