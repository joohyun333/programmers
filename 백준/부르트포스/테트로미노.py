# # https://www.acmicpc.net/problem/14500
import math

N, M = map(int, input().split())
tetris = []
for i in range(N):
    tetris.append(list(map(int, input().split())))

tetrominos = [
    # ㄹ
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    # -
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # ㅁ
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    # L
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    # ㅓ
    [(0, 0), (0, 1), (0, 2), (1, 1)],
]


def reflect(points, axis):
    new_points = []
    for y, x in points:
        if axis == 'x':
            new_points.append((-y, x))
        elif axis == 'y':
            new_points.append((y, -x))
    return new_points


def rotate(points, angle):
    new_points = []
    for y, x in points:
        angle_rad = angle * (math.pi / 180.0)
        new_x = x * round(math.cos(angle_rad)) - y * round(math.sin(angle_rad))
        new_y = x * round(math.sin(angle_rad)) + y * round(math.cos(angle_rad))
        new_points.append((new_y, new_x))
    return new_points


all_points = []
for tetromino in tetrominos:
    all_points.append(tetromino)
    all_points.append(rotate(tetromino, 90))
    all_points.append(rotate(tetromino, 180))
    all_points.append(rotate(tetromino, 270))

    reflect_x = reflect(tetromino, 'x')
    all_points.append(rotate(reflect_x, 0))
    all_points.append(rotate(reflect_x, 90))
    all_points.append(rotate(reflect_x, 180))
    all_points.append(rotate(reflect_x, 270))

    reflect_y = reflect(tetromino, 'y')
    all_points.append(rotate(reflect_y, 0))
    all_points.append(rotate(reflect_y, 90))
    all_points.append(rotate(reflect_y, 180))
    all_points.append(rotate(reflect_y, 270))

def check(y, x):
    check_answer = 0
    for a in all_points:
        is_check = 0
        size = 0
        for y_point, x_point in a:
            y_point = y_point + y
            x_point = x_point + x
            if -1 < y_point < N and -1 < x_point < M:
                is_check += 1
                size += tetris[y_point][x_point]
        if is_check == 4:
            check_answer = max(check_answer, size)
    return check_answer

answer = 0
for i in range(N):
    for j in range(M):
        new_answer = check(i, j)
        answer = max(answer, new_answer)
print(answer)
