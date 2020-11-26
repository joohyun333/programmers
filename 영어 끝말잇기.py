# https://programmers.co.kr/learn/courses/30/lessons/12981
from typing import List
def solution(n : int, words:List[str]) -> List[int]:
    turn = 1
    answer = []
    answer.append(words[0])
    for i in words[1:]:
        turn+=1
        if i not in set(answer) and answer[-1][-1:] == i[0]:
            answer.append(i)
        else:
            total_turn, rest = divmod(turn+n, n)
            if rest == 0 :
                total_turn -=1
                rest = n
            return [rest, total_turn]
            break
    if answer == words:
        return [0,0]

if __name__ == "__main__":
    n, words = 3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']
    n, words = 2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
    print(solution(n, words))