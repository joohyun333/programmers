import re
def solution(s):
    answer = [0,0]
    while s not in ["0","1"]:
        zero = len(re.findall("0", s))
        answer[1] += zero
        one = len(re.findall("1", s))
        s = bin(one)[2:]
        answer[0] += 1
    return answer


if __name__ == "__main__":
    s = "01110"
    print(solution(s))