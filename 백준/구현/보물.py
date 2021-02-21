import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
result = 0
for a, b in zip(A, B):
    result+=a*b
print(result)
