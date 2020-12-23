# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from itertools import permutations
from collections import defaultdict
def solution(begin, target, words):
    if target not in words:
        return 0
    words_list = defaultdict(list)
    n = list(permutations(range(len(words)), 2))
    def make_list(x, y):
        rest = 0
        for i in range(len(x)):
            if x[i] == y[i]:
                rest += 1
        if rest == len(x) - 1:
            words_list[x].append(y)
        return words_list
    for i in words:
        make_list(begin, i)
    for x,y in n:
        make_list(words[x],words[y])
    def dfs(w, r, graph):
        discovered = []
        stack = [w]
        index = 0
        while stack:
            v = stack.pop(0)
            if v not in discovered:
                discovered.append(v)
                for w in graph[v]:
                    stack = []
                    if w == r:
                        return index +1
                    else:
                        if w not in discovered :
                            stack.append(w)
                index+=1
        return index
    return dfs(begin, target,words_list)
if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    # words = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin,target,words))
