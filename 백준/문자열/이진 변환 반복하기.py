# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = [0, 0]
    while s != "1":
        zero = 0
        new_t = ""
        for idx, text in enumerate(s):
            if text == "0":
                zero += 1
            else:
                new_t += "1"
        answer = [answer[0] + 1, answer[1] + zero]
        s = bin(len(new_t))[2:]
    return answer


if __name__ == '__main__':
    print(solution("01110"))
