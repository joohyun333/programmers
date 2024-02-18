import math


def solution(brown, yellow):
    m = set()
    for i in range(1, yellow+1):
        if yellow % i == 0:
            num1, num2 = int(yellow / i), i
            temp = ()
            if num1 < num2:
                temp = (num2, num1)
            else:
                temp = (num1, num2)
            m.add(temp)
    answer = []
    for num1, num2 in m:
        if ((num1 + num2)*2) +4 == brown:
            answer = [num1 + 2, num2 + 2]
    return answer

if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown, yellow))

    brown = 8
    yellow = 1
    print(solution(brown, yellow))

    brown = 24
    yellow = 24
    print(solution(brown, yellow))