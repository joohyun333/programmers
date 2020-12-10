# https://www.acmicpc.net/problem/20055
from collections import deque
# n, k = map(int, input().split())
# n *= 2
# count = 0
# conveyor = list(map(int, input().split()))
# robot = [0] * n
# while conveyor.count(0) < k:
#     count += 1
#     conveyor.insert(0, conveyor.pop())
#     robot.insert(0, robot.pop())
#     robot[n // 2 - 1] = 0
#     for (r, i) in sorted([(robot[i], i) for i in range(n) if robot[i] > 0]):
#         if robot[i + 1] == 0 and conveyor[i + 1] > 0:
#             robot[i] = 0
#             robot[i + 1] = r
#             conveyor[i + 1] -= 1
#     robot[n // 2 - 1] = 0
#     if conveyor[0] > 0:
#         conveyor[0] -= 1
#         robot[0] = count + 1
# print(count)
#------------------------시간초과--------