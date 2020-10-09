# https://programmers.co.kr/learn/courses/30/lessons/60057
import re
def solution(s:str) -> int:
    m = []
    m1 = []
    result = []
    if len(s) == 1:
        return 1
        # testcase 한문자일 경우 ex)"a" return값이 []이 뜸 고로 한문자는 1로 return
    for j in range(1,(len(s)//2)+1):
        for i in range(0,len(s)+1, j):
            m.append(i)
        if m[-1] != len(s):
            m.append(len(s))
        m1.append(m)
        m = []
    # m1 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8, 10], [0, 3, 6, 9, 10], [0, 4, 8, 10], [0, 5, 10]]
    for i in range(len(m1)):
        for j in range(1, len(m1[i])):
            m.append(s[m1[i][j-1]:m1[i][j]])
        result.append(m)
        m = []
    # print(result)
    # result = [['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'], ['ab', 'ca', 'bc', 'de', 'de'], ['abc', 'abc', 'ded'], ['abca', 'bcde'], ['abcab', 'cdede']]
    answer = [] # result 값 넣으면서 answer[-1]와 문자가 겹치는지 확인하는 list
    answer_1 = [] #여기서 부터 겹치는 문자열있으면 answer_1 =  겹치는 문자열 갯수[n] + 겹치는 문자열[answer[-1]
    answer_2 = [] # 최종 답안 -> answer_1 합산해서 쳐 넣어서 여기서 가장 적은 문자열 고르기
    for i in result:
        n=1
        answer.append(i.pop(0))
        for j in i: # ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'],['ab', 'ca', 'bc', 'de', 'de'], ['abc', 'abc', 'ded']
            if answer[-1] == j:
                n+=1
                # 겹쳐지면 n+=1
            else:
                # 안 겹쳐질떈  n>1일때면 n+겹치는 문자열 넣고 n=1이면 그냥 문자열만 넣음
                if n > 1:
                    answer_1.append(str(n) + answer[-1])
                else:
                    answer_1.append(answer[-1])
                n=1
            answer.append(j)
        if n>1:
            answer_1.append(str(n) + answer[-1])
        else:
            answer_1.append(answer[-1])
        answer_2.append(len(''.join(answer_1)))
        # answer_2 = abcabcdede, abcabc2de, 2abcdede ,abcabcdede, abcabcdede 가 입력됨
        answer_1 = []
    return min(answer_2)
if __name__ == "__main__":
    s = "abcabcdede"
    # s = "aabbaccc"
    # s = "ababcdcdababcdcd"
    # # s = "abcabcabcabcdededededede"
    # # s = "xababcdcdababcdcd"
    # s = "xxxxxxxxxxyyy"
    # s = "a"
    print(solution(s))