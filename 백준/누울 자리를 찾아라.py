N = int(input())
room = []
for _ in range(N):
    y = input()
    room.append(y)
col, row = 0, 0
for i in room:
    for j in i.split("X"):
        if len(j) > 1:
            col += 1
room1 = [[0] * N for i in range(N)]
for y in range(N):
    for x in range(N):
        room1[x][y] = room[y][x]

for i in room1:
    m = ''.join(i).split("X")
    for j in m:
        if len(j) > 1:
            row += 1
print(col, row)
