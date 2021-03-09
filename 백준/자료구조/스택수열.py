from sys import stdin
n = int(stdin.readline())
in_ = [int(input()) for i in range(n)]
temp = True
cnt, stack, result = 1, [], []
for i in in_:
    print(i, cnt, stack, result)
    while cnt <= i:
        stack.append(cnt)
        result.append('+')
        cnt+=1
    if stack.pop() != i:
        temp=False
        break
    else:
        result.append('-')
if temp == False:
    print("NO")
else:
    for i in result:
        print(i)