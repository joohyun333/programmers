#https://www.acmicpc.net/problem/1629
import math

A, B, C = map(int, input().split())
answer = 1
A = A % C
while B > 0:
    if B % 2 == 1:
        answer = (answer*A)%C
    A = (A * A) % C
    B //= 2
print(answer)