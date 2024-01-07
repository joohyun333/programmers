# https://www.acmicpc.net/problem/1525
import copy
from collections import deque

puzzle = ""
for _ in range(3):
    puzzle += input().replace(" ", "")
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = {}
answer = -1
if puzzle == "123456780":
    answer = 0
q = deque()
q.append([puzzle, 0])
while q:
    puzzle_key, count = q.popleft()
    if puzzle_key == "123456780":
        answer = count
        break
    else:
        if puzzle_key not in visited:
            visited[puzzle_key] = count
            find_zero = str(puzzle_key).find("0")
            y = find_zero // 3
            x = find_zero % 3
            for dy, dx in direction:
                next_y = y + dy
                next_x = x + dx
                if -1 < next_y < 3 and -1 < next_x < 3:
                    origin = puzzle_key[next_y * 3 + next_x]
                    move = puzzle_key[find_zero]
                    new_puzzle_str = copy.deepcopy(puzzle_key)
                    new_puzzle_str = new_puzzle_str[:next_y * 3 + next_x] + move + new_puzzle_str[(next_y * 3 + next_x) + 1:]
                    new_puzzle_str = new_puzzle_str[:find_zero] + origin + new_puzzle_str[find_zero + 1:]
                    if new_puzzle_str not in visited:
                        q.append([new_puzzle_str, count + 1])

if answer == -1:
    print(-1)
else:
    print(answer)
