# https://www.acmicpc.net/problem/2174
n, m = map(int, input().split())
maps = [[0 for _ in range(n)] for _ in range(m)]
directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
directions_order = ["N", "E", "S", "W"]
robots = []
answer = []
robot_count, command_count = map(int, input().split())
for i in range(robot_count):
    x, y, direction = map(str, input().split())
    y = int(y)
    x = int(x)
    maps[m - y][x - 1] = i + 1
    robots.append([m - y, x - 1, direction])

for i in range(command_count):
    robot, command, repeat = map(str, input().split())
    y, x, d = robots[int(robot) - 1]
    d_idx = directions_order.index(d)
    complete = True
    if command == "L":
        for j in range(int(repeat)):
            y, x, d = robots[int(robot) - 1]
            d_idx = directions_order.index(d)
            robots[int(robot) - 1][2] = directions_order[d_idx - 1]
    elif command == "R":
        for j in range(int(repeat)):
            y, x, d = robots[int(robot) - 1]
            d_idx = directions_order.index(d)
            robots[int(robot) - 1][2] = directions_order[(d_idx + 1) % 4]
    elif command == "F":
        d_y, d_x = directions[d]
        pre_y, new_y = y, y
        pre_x, new_x = x, x
        for j in range(int(repeat)):
            new_y = pre_y + d_y
            new_x = pre_x + d_x
            if -1 < new_y < m and -1 < new_x < n:
                if maps[new_y][new_x] == 0:
                    maps[pre_y][pre_x] = 0
                    maps[new_y][new_x] = int(robot)
                    robots[int(robot) - 1][0] = new_y
                    robots[int(robot) - 1][1] = new_x
                    pre_y = new_y
                    pre_x = new_x
                else:
                    complete = False
                    if answer:
                        if answer[-1][0] != robot and answer[-1][2] != "c":
                            answer.append((robot, str(maps[new_y][new_x]), "c"))
                    else:
                        answer.append((robot, str(maps[new_y][new_x]), "c"))
            else:
                complete = False
                if not answer:
                    answer.append((robot, "wall", "w"))
                else:
                    if answer[-1][0] != robot and answer[-1][2] != "w":
                        answer.append((robot, "wall", "w"))
    if not complete:
        break

if not answer:
    print("OK")
else:
    for robo, to_answer, reason in answer:
        if reason == "w":
            print("Robot " + robo + " crashes into the wall")
        else:
            print("Robot " + robo + " crashes into robot " + to_answer)
