from typing import List
import re
def solution(s :str) -> List[int]:
    sentence = sorted(eval(re.sub("[}]","]",re.sub("[{]","[",s))),key = len)
    answer = []
    answer.append(sentence.pop(0)[0])
    for i in sentence:
        inter = set(i) - set(answer)
        answer.append(inter.pop())
    return answer


if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))