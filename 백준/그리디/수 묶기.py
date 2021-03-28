# https://www.acmicpc.net/problem/1744
import sys
input = sys.stdin.readline
a = [int(input()) for _ in range(int(input()))]
a.sort()
minus = []
plus = []
for i in a:
    if i<=0:
        minus.append(i)
    else:
        plus.append(i)

total = 0
while plus:
    if plus[0]==1:
        plus.pop(0)
        total+=1
    else:
        break

while len(plus)>1:
    a = plus.pop()
    b = plus.pop()
    total+=(a*b)

while len(minus)>1:
    a = minus.pop(0)
    b = minus.pop(0)
    total+=(a*b)


print(total+sum(minus)+sum(plus))
