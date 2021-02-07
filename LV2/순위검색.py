from typing import List
import collections
import itertools
def solution(info, query):
    interview = collections.defaultdict(list)
    answer = []
    for i in info:
        m = i.split(" ")
        m_strs = ""
        for j in m:
            if j.isdigit(): interview[m_strs].append(int(j))
            m_strs += j
    memo_dic = [["cpp", "java","python"],["backend","frontend"],["junior","senior"],["chicken","pizza"]]
    memo_list = []
    for q in query:
        m = q.replace("and", "").replace("  ", " ").split(" ")
        score = int(m.pop())
        m_strs = []
        result = 0
        for i, e in enumerate(m):
            if e =="-" :
                m_strs.append(memo_dic[i])
            else:m_strs.append([e])
        memo = itertools.product(m_strs[0],m_strs[1],m_strs[2],m_strs[3])
        for n in list(memo):
            for v in interview[''.join(n)]:
                if v>=score:
                    result+=1
        answer.append(result)
    return answer


if __name__ == "__main__":
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))
    # [1,1,1,1,2,4]
