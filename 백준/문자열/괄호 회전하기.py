# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3
from collections import deque
def solution(s):
    str_dic = {"}":"{", ")":"(","]":"["}
    t = deque(s)
    count = 0
    answer = 0
    while count != len(s)-1:
        stack = []
        is_str = True
        for idx, text in enumerate(t):
            if not stack:
                stack.append(text)
            else:
                if text == "(" or text == "[" or text == "{" :
                    stack.append(text)
                else:
                    if stack[-1] == str_dic[text]:
                        stack.pop()
                    else:
                        is_str = False
                        break
        if is_str and len(stack) == 0:
            answer += 1
        count += 1
        t.append(t.popleft())

    return answer

if __name__ == '__main__':
    print(solution("[](){}"))
    print(solution("[)(]"))
    print(solution("}}}"))