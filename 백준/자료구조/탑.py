# https://www.acmicpc.net/problem/2493
n = int(input())
towers = list(map(int, input().split()))
stack = []

answer = []
for idx, tower in enumerate(towers):
    while stack:
        if stack[-1][1] > tower:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append((idx, tower))
print(" ".join(map(str, answer)))