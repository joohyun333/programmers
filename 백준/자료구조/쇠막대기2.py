# https://www.acmicpc.net/problem/10799
steels = list(input().replace("()", "|"))
floor = 0
answer = 0
for i in steels:
    if i == "(":
        floor += 1
    elif i == "|":
        answer += floor
    else:
        answer += 1
        floor -= 1
print(answer)
