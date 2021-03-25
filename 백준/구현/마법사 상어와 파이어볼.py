# https://www.acmicpc.net/problem/20056
import collections, copy, sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
ball = collections.defaultdict(list)
for i in range(M):
    r, c, *data = map(int, input().split())
    ball[(r - 1, c - 1)].append(data)


def direction(p, repeat, n):  # 위치, 속력, 방향
    y, x = p[0], p[1]
    up_y, up_x = (N + y + (repeat % N)) % N, (N + x + (repeat % N)) % N
    down_y, down_x = (N + y - (repeat % N)) % N, (N + x - (repeat % N)) % N

    if n == 0:
        y = down_y
    elif n == 1:
        y = down_y
        x = up_x
    elif n == 2:
        x = up_x
    elif n == 3:
        y = up_y
        x = up_x
    elif n == 4:
        y = up_y
    elif n == 5:
        y = up_y
        x = down_x
    elif n == 6:
        x = down_x
    elif n == 7:
        y = down_y
        x = down_x
    return y, x


def move():
    for b in ball:
        for m, s, d in ball[b]:
            y, x = direction((b[0], b[1]), s, d)
            new_ball[(y, x)].append((m, s, d))


def combine():
    change = copy.deepcopy(new_ball)
    for i in new_ball:
        if len(new_ball[i]) >= 2:
            total_m, total_s, total_d = 0, 0, []
            for m, s, d in new_ball[i]:
                total_m += m
                total_s += s
                total_d.append(d%2)
            total_m = total_m // 5
            total_s = total_s // len(new_ball[i])
            total = []
            if total_m == 0:
                change[i].clear()
            else:
                if len(set(total_d)) == 1:
                    for di in [0, 2, 4, 6]:
                        total.append((total_m, total_s, di))
                else:
                    for di in [1, 3, 5, 7]:
                        total.append((total_m, total_s, di))
                change[i] = total
    return change


for _ in range(K):
    new_ball = collections.defaultdict(list)
    move()
    new_ball = combine()
    ball = new_ball

result = 0
for b in ball:
    for m, s, d in ball[b]:
        result += m
print(result)
