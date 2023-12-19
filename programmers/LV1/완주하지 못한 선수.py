# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution1(participant, completion):
    dict ={}
    sumHah=0
    for p in participant:
        dict[hash(p)] = p
        sumHah+=hash(p)

    for c in completion:
        sumHah-=hash(c)
    return dict[sumHah]
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution2(participant, completion))
    # print(solution(participant, completion))
