# https://programmers.co.kr/learn/courses/30/lessons/42842
import math
def solution(brown, yellow):
    total = brown + yellow
    total_list = []
    for i in range(3, int(math.sqrt(total))+1):
        if total % i == 0:
            total_list.append([total//i,i])
    for i, e in total_list:
        if (((i+e)*2)-4) == brown and ((i-2)*(e-2)) == yellow:
            return [i,e]

# 다른 사람 코드 -  기본적인 로직은 같으나 더 간결함.
# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]

if __name__ == "__main__":
    b = 8
    y = 1
    print(solution(b,y))