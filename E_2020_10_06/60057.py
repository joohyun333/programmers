# https://programmers.co.kr/learn/courses/30/lessons/60057
import re
def solution(s):
    bask = []
    answer = []
    while s:
        s_list = [s[0:i] for i in range(1, (len(s) // 2) + 1)]
        for i in range(len(s_list)):
            m = re.findall(s_list[i], s)
            if len(m)>1 and m[0][0] == s[0]:
                bask.append(m)
            else:
                break
        if bask:
            answer.append(str(len(bask[-1]))+bask[-1][0])
            s = s.replace(bask[-1][0], "")
            bask.clear()
        else:
            answer.append(s)
            break
    return len(''.join(answer))

if __name__ == "__main__":
    s = "abcabcdede"
    print(solution(s))