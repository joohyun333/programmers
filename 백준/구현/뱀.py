#https://www.acmicpc.net/problem/3190
from collections import deque
n = int(input())
board = []
val = 0
for i in range(n+2):
    if i == 0 or i == n+1:
        val = -1
    else:
        val = 0
    data = [-1]
    for j in range(n):
        data.append(val)
    data.append(-1)
    board.append(data)
del data, val
for i in range(int(input())):
    y, x = map(int, input().split())
    board[y][x] = 1
answer = 0
directions = [(0,1),(1,0),(0,-1),(-1,-0)]
new_d = 0
snake = (1,1)
discovered = deque([[1,1]])
length = 1
pre_count = 0
move = int(input())
for i in range(move+1):
    count = 0
    direction = ''
    if i == move:
        count, direction, pre_count = n, 'D', 0
    else:
        count, direction = input().split()
    for _ in range(int(count) - pre_count):
        answer += 1
        dy, dx = directions[new_d]
        sy, sx = snake[0] + dy, snake[1] + dx

        if board[sy][sx] == -1 :
            print(answer)
            exit(0)
        elif board[sy][sx] == 1 :
            length += 1

        if len(discovered) == length:
            y, x = discovered.popleft()
            board[y][x] = 0
            board[sy][sx] = -1
        else:
            board[sy][sx] = -1
        discovered.append([sy, sx])
        snake = (sy, sx)
    pre_count = int(count)
    if direction == 'L':
        new_d = (new_d - 1) % 4
    else:
        new_d = (new_d + 1) % 4