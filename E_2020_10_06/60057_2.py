# https://programmers.co.kr/learn/courses/30/lessons/60057
import re
def solution(s):
    m = []
    m1 = []
    result = []
    if len(s) == 1:
        return 1
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
    answer = []
    answer_1 = []
    answer_2 = []
    for i in result:
        n=1
        answer.append(i.pop(0))
        for j in i: # ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'], ['abc', 'abc', 'ded']
            if answer[-1] == j:
                n+=1
            else:
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
        answer_1 = []
    return min(answer_2)
if __name__ == "__main__":
    s = "abcabcdede"
    s = "aabbaccc"
    s = "ababcdcdababcdcd"
    # s = "abcabcabcabcdededededede"
    # s = "xababcdcdababcdcd"
    s = "xxxxxxxxxxyyy"
    s = "a"
    print(solution(s))