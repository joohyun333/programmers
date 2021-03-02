import collections
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
discoverd = [False] * (F + 1)
queue = collections.deque([[S, 0]])
result = -1
while queue:
    q, c = queue.popleft()
    if q == G:
        result = c
        break
    else:
        if 0 < q <= F and not discoverd[q]:
            discoverd[q] = True
            queue.append([q + U, c + 1])
            queue.append([q - D, c + 1])
if result>=0:
    print(result)
else:
    print("use the stairs")