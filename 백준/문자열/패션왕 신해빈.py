#https://www.acmicpc.net/problem/9375
from itertools import combinations
for _ in range(int(input())):
    case = int(input())
    case_dic = {}
    for i in range(case):
        a,b = input().split()
        if not case_dic.get(b):
            case_dic[b] = 1
        else:
            case_dic[b] += 1
    answer = 1
    for i in case_dic:
        answer *= case_dic[i]+1
    print(answer-1)