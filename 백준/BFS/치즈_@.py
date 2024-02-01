# https://www.acmicpc.net/problem/2636
from collections import deque
y, x = map(int, input().split())
data = []
c_count = 0
for i in range(y):
    d = list(map(int, input().split()))
    data.append(d)
    c_count += d.count(1)

direction = [(-1,0),(1,0),(0,-1),(0,1)]
turn = 0
answer = [c_count]
while c_count > 0:
    turn += 1
    c = 0
    q = deque([[0, 0]])
    visited = [[False for i in range(x)] for j in range(y)]
    around = set()
    while q:
        qy, qx = q.popleft()
        for dy, dx in direction:
            if -1 < qy+dy < y and -1 < qx+dx < x and not visited[qy+dy][qx+dx]:
                if data[qy+dy][qx+dx] == 0:
                    visited[qy+dy][qx+dx] = True
                    q.append([qy+dy, qx+dx])
                else:
                    around.add((qy+dy, qx+dx))
    for ay, ax in around:
        data[ay][ax] = 0
        c_count -= 1
    if c_count != 0:
        answer.append(c_count)

print(turn)
print(answer[-1])
