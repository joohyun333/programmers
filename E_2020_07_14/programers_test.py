# https://programmers.co.kr/learn/courses/30/lessons/42840
# def solution(answers):
#     answer= [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
#     answer_num = [0,0,0]
#     for i, j in enumerate(answers) :
#         for x,y in enumerate(answer):
#             if j == y[i%len(y)]:
#                 answer_num[x] += 1
#     return [num1 + 1 for num1, num2 in enumerate(answer_num) if y == max(answer_num)]

def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0,0,0]

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
if __name__ == "__main__" :
    answer = [1,3,2,4,2,4]
    print(solution(answer))