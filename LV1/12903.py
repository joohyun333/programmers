# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s)//2)-1:(len(s)//2)+1] # 이건 주석 달것도 없다 ㅇㅈ?
    else:
        return s[(len(s)//2)]

if __name__ == "__main__":
    s = "abcd"
    print(solution(s))