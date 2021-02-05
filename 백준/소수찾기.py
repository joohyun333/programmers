import sys
import math
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
m = [True] * 1001
m[0],m[1]= False, False
for j in range(2, int(math.sqrt(1000)+1)):
    for i in range(j+j, 1001, j):
        if m[i]:
            m[i] = False
result = 0
for n in arr:
    if m[n]: result += 1
print(result)
