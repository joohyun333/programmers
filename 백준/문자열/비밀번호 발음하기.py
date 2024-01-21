# https://www.acmicpc.net/problem/4659
while True:
    t = input()
    if t == "end":
        break
    c_1, c_2, c_3 = False, True, True
    mo_count, za_count = 0, 0
    pre_text = ""
    c_3_con = 0
    for idx, text in enumerate(t):
        if text in ['a', 'e', 'i', 'o', 'u']:
            c_1 = True
            mo_count += 1
            if mo_count > 2:
                c_2 = False
                break
            za_count = 0
        else:
            za_count += 1
            if za_count > 2:
                c_2 = False
                break
            mo_count = 0
        if text not in ['e', 'o'] and text == pre_text and c_3_con == 1:
            c_3 = False
            break
        if pre_text == text:
            c_3_con += 1
        else:
            pre_text = text
            c_3_con = 1

    if c_1 and c_2 and c_3:
        print("<" + t + "> is acceptable.")
    else:
        print("<" + t + "> is not acceptable.")
