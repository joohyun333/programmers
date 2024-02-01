# # https://www.acmicpc.net/problem/22942
# data = []
# for i in range(int(input())):
#     x, r = map(int, input().split())
#     data.append([x - r, i])
#     data.append([x + r, i])
# data = sorted(data)
# stack = []
# for point, d_idx in data:
#     if stack:
#         if stack[-1][1] == d_idx:
#             stack.pop()
#         else:
#             stack.append((point, d_idx))
#     else:
#         stack.append((point, d_idx))
# print("NO" if stack else "YES")
import sys

def solution(): #O(N^2)
    circles = []

    #N = int(input())

    N = int(sys.stdin.readline())
    #input_lst = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        x, r = list(map(int, sys.stdin.readline().split()))
        circles.append((x-r,i))
        circles.append((x+r,i))
    circles.sort() # 핵심 : 겹치는 구간이 생길 경우 circles 순서와 달라진다!!

    stack = []
    for c in circles:
        if stack :
            if stack[-1][1] == c[1]: #같은 원의 시작과 끝일 경우 (원 인덱스가 같을 경우)
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    if stack:
        return "NO"
    return "YES"

print(solution())