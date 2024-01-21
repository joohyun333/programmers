import string
answer = []
for _ in range(int(input())):
    s = list(input()+"z")
    temp = ""
    for j in s:
        if j in string.digits:
            temp += j
        else:
            if temp != "":
                answer.append(int(temp))
                temp = ""
for i in sorted(answer):
    print(i)