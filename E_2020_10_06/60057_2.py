# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    m = []
    m1 = []
    result = []
    for j in range(1,(len(s)//2)+1):
        for i in range(0,len(s)+1, j):
            m.append(i)
        m1.append(m)
        m = []
    # m1 = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8, 10], [0, 3, 6, 9], [0, 4, 8], [0, 5, 10]]
    for i in range(len(m1)):
        for j in range(1, len(m1[i])):
            m.append(s[m1[i][j-1]:m1[i][j]])
        result.append(m)
        m = []
    # result = [['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'], ['ab', 'ca', 'bc', 'de', 'de'], ['abc', 'abc', 'ded'], ['abca', 'bcde'], ['abcab', 'cdede']]
    answer = []
    answer_1 = []
    answer_2 = []
    for i in range(len(result)):
        answer_1.append(result[i][0])
        while len(result[i])>1: # ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'd', 'e'], ['abc', 'abc', 'ded']
            if answer_1[-1:] != result[]:
                answer_1.append(get_num)
            else:
                answer_2.append(get_num)

            answer.append(get_num)
    return answer

if __name__ == "__main__":
    s = "abcabcdede"
    print(solution(s))