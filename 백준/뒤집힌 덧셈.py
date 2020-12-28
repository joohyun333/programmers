# https://www.acmicpc.net/problem/1357
a, b = input().split()
print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))