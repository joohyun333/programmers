from collections import deque
import math


def rotate(points, angle):
    new_points = []
    for idx, val in enumerate(points):
        y, x = val[0], val[1]
        angle_rad = angle * (math.pi / 180.0)
        new_x = x * round(math.cos(angle_rad)) - y * round(math.sin(angle_rad))
        new_y = x * round(math.sin(angle_rad)) + y * round(math.cos(angle_rad))
        new_points.append((new_y, new_x))
    return new_points

def solution(game_board, table):
    ps = []
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(len(game_board[0]))] for _ in range(len(game_board))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1 and not visited[i][j]:
                p = [[i, j]]
                q = deque([[i, j]])
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ny, nx = dy + y, dx + x
                        if -1 < ny < len(table) and -1 < nx < len(table[0]) and not visited[ny][nx] and table[ny][nx] == 1:
                            visited[ny][nx] = True
                            q.append([ny, nx])
                            p.append([ny, nx])
                tamp_p = []
                for point_y, point_x in p :
                    tamp_p.append([point_y-p[0][0], point_x-p[0][1]])
                ps.append(tamp_p)

    result = 0
    use_ps = [False for _ in range(len(ps))]
    visited = [[False for _ in range(len(game_board[0]))] for _ in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and not visited[i][j]:
                q = deque([[i, j]])
                visited[i][j] = True
                blank = [[i,j]]
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        ny, nx = dy + y, dx + x
                        if -1 < ny < len(game_board) and -1 < nx < len(game_board[0]) and game_board[ny][nx] == 0 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append([ny, nx])
                            blank.append([ny, nx])

                for idx, p in enumerate(ps):
                    if not use_ps[idx]:
                        is_search = False
                        if len(p) == len(blank):
                            for angle in [0, 90, 180, 270]:
                                rotate_p = sorted(rotate(p, angle))
                                blank_temp = sorted(blank)
                                diff_y, diff_x = blank_temp[0][0] - rotate_p[0][0], blank_temp[0][1] - rotate_p[0][1]
                                blank_count = len(blank)
                                for r in rotate_p:
                                    if [r[0] + diff_y, r[1] + diff_x] in blank_temp:
                                        blank_count -= 1
                                if blank_count == 0:
                                    result += len(p)
                                    is_search = True
                                    use_ps[idx] = True
                                    break
                        if is_search:
                            break
    return result
if __name__ == '__main__':
    game_board = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    print(solution(game_board, table))

    game_board = [[0,0,0],[1,1,0],[1,1,1]]
    table = [[1,1,1],[1,0,0],[0,0,0]]
    print(solution(game_board, table))