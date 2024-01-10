n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]
for idx, num in enumerate(a):
    while stack:
        if stack[-1][1] < num:
            answer[stack[-1][0]] = num
            stack.pop()
        else:
            stack.append((idx, num))
            break
    if not stack:
        stack.append((idx, num))
print(' '.join(map(str, answer)))