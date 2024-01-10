answer = 0
for i in range(1, int(input()) + 1):
    if i < 100:
        answer += 1
    else:
        str_num = str(i)
        temp = int(str_num[1]) - int(str_num[0])
        is_true = True
        for idx in range(2, len(str_num)):
            if temp != (int(str_num[idx]) - int(str_num[idx - 1])):
                is_true = False
                break
        if is_true:
            answer += 1
print(answer)