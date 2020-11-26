# https://programmers.co.kr/learn/courses/30/lessons/42890
from typing import List
from itertools import combinations
def solution(relation:List) ->int:
    index = []
    for i in range(1,len(relation[0])+1):
        index.append(list(map(list,combinations(range(len(relation[0])),i))))
    index = sum(index, [])
    result = []
    for i in index:
        counter = []
        for relations in relation:
            counter.append(''.join(map(str,[relations[j] for j in i])))
        if len(set(counter)) == len(relation):
            result.append(i)
    result_answer = result.copy()
    for i in range(len(result)-1) :
        for j in range(i+1, len(result)):
            if set(result[i]) == set(result[i]) & set(result[j]) and result[j] in result_answer:
                result_answer.remove(result[j])
    return len(result_answer)

if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    print(solution(relation))
