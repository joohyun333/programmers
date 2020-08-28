# https://programmers.co.kr/learn/courses/30/lessons/67257
def solution(expression):
    sign = ["+", "-", "*"]
    sign_position = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]] # 우선순위

    for i, e in enumerate(expression):
        if sign in e:
            ㅌ``


    return expression

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))