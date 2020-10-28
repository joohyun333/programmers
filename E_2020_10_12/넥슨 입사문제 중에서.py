# # https://codingdojang.com/scode/365
# def solution():
#     answer =[]
#     for i in range(5000):
#         num =sum([int(i) for i in list(str(i))]) + i
#         print(num)
#         answer.append(num)
#     return answer
# if __name__ == "__main":
#     print(solution())
answer =[sum([int(i) for i in list(str(i))]) + i for i in range(1,5000) if sum([int(i) for i in list(str(i))]) + i < 5000]
print(sum(set(i for i in range(1,5000)) - set(answer)))
print(sorted(set(i for i in range(1,100)) - set(answer)))