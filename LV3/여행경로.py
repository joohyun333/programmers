# https://programmers.co.kr/learn/courses/30/lessons/43164
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(100)
# def solution(tickets, plus=[]):
#     a = defaultdict(list)
#     for i in sorted(tickets):
#         a[i[0]].append(i[1])
    # def dfs(v, discovered=[]):
    #     discovered.append(v)
    #     for w in a[v]:
    #         if w in a[v]:
    #             a[v].remove(w)
    #             discovered = dfs(w, discovered)
    #     return discovered
    # z = dfs("ICN")
    # print(a)
    # if len(z) == len(tickets)+1 and z:
    #     return z+plus
    # else:
    #     for i in range(1, len(z)):
    #         tickets.remove([z[i-1],z[i]])
    #     return solution(tickets, z[1:])
#---------------재귀로 푸는게 아닌듯 함....0.75%통과-----------------
from collections import defaultdict
from typing import List
def solution(tickets:List[str]) -> List[str]:
    data = defaultdict(list)
    for i in sorted(tickets, reverse=True):
        data[i[0]].append(i[1])
    link, not_link = ['ICN'], []
    while link:
        search = link[-1]
        if search not in data or len(data[search])==0:
            not_link.append(link.pop())
        else:
            link.append(data[search].pop())
    not_link.reverse()
    return not_link
if __name__ == "__main__":
    # tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets = [["ICN", "BOO"], ["BOO", "COO"], ["COO", "ICN"]]
    tickets = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
    print(solution(tickets))