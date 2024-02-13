t = input()
bomb = input()
if len(t) < len(bomb):
    print(t)
elif len(t) == len(bomb):
    if t == bomb:
        print("FRULA")
    else:
        print(t)
else:
    stack = list(t[:len(bomb) - 1])
    for i in range(len(bomb)-1, len(t)):
        temp = ''.join(stack[len(stack)-(len(bomb)-1):])
        if temp + t[i] == bomb:
            for _ in range(len(bomb)-1):
                stack.pop()
        else:
            stack.append(t[i])
    if not stack:
        print("FRULA")
    else:
        print(''.join(stack))