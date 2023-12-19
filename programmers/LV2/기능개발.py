# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
import math
def solution(progresses, speeds):
    stack = []
    for i, e in enumerate(progresses):
        if speeds[i] == 0 :
            a = math.ceil(100 - e)
            stack.append(a)
        else:
            a = math.ceil((100 - e) / speeds[i])
            stack.append(a)

    stack = stack[::-1]
    a = stack.pop()
    n = 1
    result = []
    while stack:
        if a >= stack[-1]:
            stack.pop()
            n += 1
        else:
            result.append(n)
            a = stack.pop()
            n = 1
    result.append(n)
    return result

if __name__ == "__main__":
    progresses, speeds = [99],[0]
    print(solution(progresses,speeds))