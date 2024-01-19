answer = 0
for i in range(int(input())):
    a = input()
    stack = []
    for j in a:
        if stack:
            if stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)
        else:
            stack.append(j)
    if not stack:
        answer += 1
print(answer)