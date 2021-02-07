from typing import List,Dict
import collections
import itertools
import bisect
def solution(info:List[str], query:List[str]) -> List[int]:
    interview:Dict[str, int] = collections.defaultdict(list)
    answer:List[int] = [0]*len(query)
    for i in info:
        m = i.split(" ")
        m_strs = ""
        for j in m:
            if j.isdigit():
                interview[m_strs].append(int(j))
                interview[m_strs].sort() # 효율성 통과(이진탐색)를 위한 코테점수 오름차순 정렬(지원자마다)
            m_strs += j
    memo_dic:List[str] = [["cpp", "java","python"],["backend","frontend"],["junior","senior"],["chicken","pizza"]]
    for q_i, q in enumerate(query):
        m:str = q.replace("and", "").replace("  ", " ").split(" ")
        score:int = int(m.pop())
        m_strs:List[List[str]] = []
        for i, e in enumerate(m):
            if e =="-" :
                m_strs.append(memo_dic[i])
            else:m_strs.append([e])
        memo:List[str] = itertools.product(m_strs[0],m_strs[1],m_strs[2],m_strs[3])
        for n in list(memo):
            n_list:int = interview[''.join(n)]
            answer[q_i]+=(len(n_list) - bisect.bisect_left(n_list,score))
            # 이진탐색 메소드 (bisect.bisect_left(List, int)-> List중에 int 값이 들어갈 index반환,
            # 이진탐색을 통해 같은 숫자일시 왼쪽 인덱스 줌 -> bisect.bisect_left([4,4], 4)일시 0 반환
            # (bisect.bisect_right, bisect.bisect)은 오른쪽 인덱스 줌
            # n_list 전체 길이 - n_list내에 score가 들어갈 index = n_list에는 score보다 큰 코테점수만 남음
            # 0부터 len(n_list) 조사 할시 효율성 테스트 못함.
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
