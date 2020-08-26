from itertools import permutations
def solution(numbers):
    answer_list = []
    answer = ''
    # numbers = numbers.replace("[","").replace("]","")
    # numbers = list(map(int, numbers.split(",")))
    for i in list(permutations(numbers, len(numbers))):
        for j in range(len(numbers)):
            answer += str(i[j])
        answer_list.append(answer)
        answer = ''
    return str(max(answer_list))

if __name__ == "__main__":
    a = input()
    print(solution(a))
# from itertools import permutations
from itertools import combinations
# def solution(a):
#     print(type(a))
#     print(a)
#
# print(solution(b))
# a = []
# b = ''
# items= input()
# print(len(items))
# for i in list(permutations(items,len(items))):
#     for j in range(len(items)):
#         b += str(i[j])
#     a.append(b)
#     b = ''
# print(max(a))