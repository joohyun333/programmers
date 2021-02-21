import sys

input = sys.stdin.readline
row, col = map(int, input().split())
cheese = [[0] * (col + 2)]
for i in range(row):
    b = [0]
    r = list(map(int, input().split()))
    r.extend([0])
    b.extend(r)
    cheese.append(b)
cheese.append([0] * (col + 2))

def bfs():
    v = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0, 0)]
    index_1 = []
    discovered = [[False]*(col+2) for _ in range(row+2)]
    while queue:
        n_x, n_y = queue.pop()
        index = [(n_x + x, n_y + y) for x, y in v if 0 <= n_x + x < row+2 and 0 <= n_y + y < col+2]
        for i_x, i_y in index:
            if not discovered[i_x][i_y]:
                discovered[i_x][i_y] = True
                if cheese[i_x][i_y] == 1 :
                    index_1.append((i_x, i_y))
                else:
                    queue.append((i_x, i_y))
    return index_1


count, rest = 0, []
while True:
    search_1 = bfs()
    if not search_1:
        print(count)
        print(rest[-1])
        break
    count += 1
    rest.append(len(search_1))
    for s_x, s_y in search_1:
        cheese[s_x][s_y] = 0
