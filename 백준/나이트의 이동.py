# https://www.acmicpc.net/problem/7562
import sys
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    I = int(input())
    start_x, start_y = input().split()
    goal_x, goal_y = input().split()
    route = [[0] * I for i in range(I)]
    route[0][0] = 1
    queue = [(0, 0)]
    while queue:
        v_x, v_y = queue.pop(0)
        if v_x == goal_x and v_y == goal_y:
            break
        for (i, j) in filter(lambda t: t[0] in range(I) and t[1] in range(I),
                             [(v_x -2, v_y+1), (v_x - 1, v_y), (v_x, v_y + 1), (v_x, v_y - 1)]):
            if route[i][j] == 0:
                route[i][j] = route[v_x][v_y] + 1
                queue.append((i, j))
