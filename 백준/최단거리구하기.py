user_input = int(input())
arr = []
for _ in range(user_input):
    arr.append(list(map(int, input().split())))
queue = [(0,0,0)]
go = [(1,0),(-1,0),(0,1),(0,-1)]
while queue:
    x, y, c = queue.pop(0)
    if x == user_input-1 and y == user_input-1:
        print(c+1)
        break
    if arr[x][y] == 1:
        arr[x][y] = 0
        for gx, gy in go:
            if 0<=x+gx<user_input and 0<=y+gy<user_input:
                queue.append((x+gx, y+gy, c+1))