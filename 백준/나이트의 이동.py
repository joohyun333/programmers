import sys
import collections
input = sys.stdin.readline
N = int(input())
v = [(1,2),(2,1),(1,-2),(2,-1),(-1,-2),(-2,-1),(-2,1),(-1,2)]
for _ in range(N):
    n = int(input())
    discovered = [[False]*n for _ in range(n)]
    queue = collections.deque()
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    start.append(0)
    queue.append(start)
    discovered[start[0]][start[1]] = True
    while queue:
        borad_y,borad_x, count = queue.popleft()
        if borad_y == end[0] and borad_x == end[1]:
            print(count)
            break
        index = [(borad_y+y, borad_x+x) for y,x in v if 0<=borad_y+y<n and 0<=borad_x+x<n]
        for i_y, i_x in index:
            if not discovered[i_y][i_x]:
                discovered[i_y][i_x] = True
                queue.append([i_y,i_x, count+1])