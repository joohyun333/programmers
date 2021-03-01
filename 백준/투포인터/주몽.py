import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
num = list(map(int, input().split()))
result = 0
for i in num:
    if M-i in num:
        result+=1
print(result//2)