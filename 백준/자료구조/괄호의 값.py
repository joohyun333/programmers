# https://www.acmicpc.net/problem/2504
from collections import deque

data = input()
temp = 1
answer = 0
stack = []
for idx, d in enumerate(data):
    if d == "(" :
        temp *= 2
        stack.append(d)
    if d == "[":
        temp *= 3
        stack.append(d)
    elif d == ")":
        if not stack or stack[-1] != "(":
            answer = 0
            break
        if data[idx - 1] == "(":
            answer += temp
        stack.pop()
        temp = temp // 2

    elif d == "]":
        if not stack or stack[-1] != "[":
            answer = 0
            break
        if data[idx - 1] == "[":
            answer += temp
        stack.pop()
        temp = temp // 3
if stack:
    print(0)
else:
    print(answer)