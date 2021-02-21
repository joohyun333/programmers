# https://www.acmicpc.net/problem/10867
import sys
input = sys.stdin.readline
N = int(input())
for i in sorted(set(map(int, input().split()))):
    print(i, end=' ')
