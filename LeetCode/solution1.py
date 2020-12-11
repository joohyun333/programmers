def solution(participant, completion):
    a = collections.Counter(participant) - collections.Counter(completion)
    ab = a.keys()
    return ''.join(ab)

import collections

if __name__ == "__main__":
    a = input()
    b = input()
    print(solution(a ,b))
    solution()

