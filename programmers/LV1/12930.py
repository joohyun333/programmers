# https://programmers.co.kr/learn/courses/30/lessons/12930
# # 이건 주석 달것도 없다 ㅇㅈ?
def solution(s):
    answer = list(s.split(" "))
    a = ""
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j % 2 == 0:
                a+=answer[i][j].upper()
            else:
                a+=answer[i][j].lower()
        a += " "
    return a[:-1]

if __name__ == "__main__":
    s ="try hello world"
    print(solution(s))
