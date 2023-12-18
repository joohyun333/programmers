# https://www.acmicpc.net/problem/2583
import sys
from collections import deque

data = input().split()
N, M,  K = int(data[0]), int(data[1]), int(data[2])
area = [[False] * M for _ in range(N)]
for i in range(K):
    ban_area = input().split()
    for j in range(int(ban_area[0]), int(ban_area[1])):
        for z in range(int(ban_area[2]-1), int(ban_area[3])):
            area[j][z] = True
answer_count = 0
answer_size = []
node = deque([(0, 0)])
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while node:
    s = node.popleft()
    for i in direction:
        nextN, nextM = int(i[0] + s[0]), int(i[1] + s[1])
        if area[nextN][nextM]:
            answer_count += 1
            size = 0
            area_node = deque([(nextN, nextM)])
            while area_node:
                a = area_node.popleft()
                area_N, area_M = a[0], a[1]
                if area[area_N][area_M]:
                    size += 1
                    area[area_N][area_M] = False
                for j in direction:
                    area_nextN, area_nextM = int(j[0] + s[0]), int(j[1] + s[1])
                    if area[area_nextN][area_nextM]:
                        area_node.append(area_nextN, area_nextM)

print(answer_count)
print(sorted(answer_size))