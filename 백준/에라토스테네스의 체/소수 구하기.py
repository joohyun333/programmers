import sys
import math
input = sys.stdin.readline
s, e = list(map(int, input().split()))
m = [True] * (e+1)
m[0],m[1]= False, False
for j in range(2, int(math.sqrt(e)+1)):
    for i in range(j+j, e+1, j):
        if m[i]:
            m[i] = False
for n in range(s, e+1):
    if m[n]: print(n)
