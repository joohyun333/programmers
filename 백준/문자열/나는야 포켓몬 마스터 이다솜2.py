# https://www.acmicpc.net/problem/1620
import string
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic_num = {}
dic = {}
for i in range(1, N + 1):
    p = input().strip('\n')
    dic_num[p] = i
    dic[i] = p
for i in range(M):
    p = input()
    if p[0] in string.digits:
        print(dic[int(p)])
    else:
        print(dic_num[p.strip('\n')])
