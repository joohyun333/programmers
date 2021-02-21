N = int(input())
data = []
for i in range(N):
        data.append(list(input()))
distnace = [(0,1),(0,-1),(1,0),(-1,0)]
discoverd = [[False]*N for _ in range(N)]
queue = []
total_count = count = 0
result = []
for i in range(N):
    for j in range(N):
        if data[i][j] == "1":
            queue.append((i, j))
            total_count +=1
            count = 0
            while queue:
                m = queue.pop(0)
                if not discoverd[m[0]][m[1]] and data[m[0]][m[1]] == "1":
                    count+=1
                    data[m[0]][m[1]] = "0"
                    discoverd[m[0]][m[1]] = True
                    for z in distnace:
                        if 0<=z[0]+m[0]<N and 0<=z[1]+m[1]<N:
                            queue.append((z[0]+m[0],z[1]+m[1]))
            result.append(count)
print(total_count)
for i in sorted(result):
    print(i)
