# https://www.acmicpc.net/problem/14891
from collections import deque

wheels = []
for i in range(4):
    wheels.append(deque(list(input())))


def is_change(w_idx, d):
    change = [0, 0, 0, 0]
    change[w_idx] = d
    start_point = w_idx - 1
    end_point = w_idx + 1
    for s in range(start_point, -1, -1):
        wheel = wheels[s]
        if wheels[s + 1][6] != wheel[2]:
            if change[s + 1] == 1:
                change[s] = -1
            elif change[s + 1] == -1:
                change[s] = 1
    for e in range(end_point, 4):
        wheel = wheels[e]
        if wheels[e - 1][2] != wheel[6]:
            if change[e - 1] == 1:
                change[e] = -1
            elif change[e - 1] == -1:
                change[e] = 1
    return change


for i in range(int(input())):
    wheel_idx, direction = map(int, input().split())
    wheel_idx = wheel_idx - 1
    change_arr = is_change(wheel_idx, direction)
    for c_dix, c in enumerate(change_arr):
        pre_wheel = wheels[c_dix]
        if c == 1:
            w = pre_wheel.pop()
            pre_wheel.insert(0, w)
            wheels[c_dix] = pre_wheel
        elif c == -1:
            w = pre_wheel.popleft()
            pre_wheel.append(w)
            wheels[c_dix] = pre_wheel
bin_str = "0b"
for idx in range(3, -1, -1):
    bin_str += wheels[idx][0]
print(int(bin_str, 2))