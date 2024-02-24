# def find_combinations(nums):
#     result = []
#     n = len(nums)
#
#     # 부분 수열을 생성하는 반복문
#     for i in range(1, 2**n):
#         subset = [nums[j] for j in range(n) if (i >> j) & 1]
#         result.append(subset)
#
#     return result
#
# def find_combination_to_target(nums):
#     all_combinations = find_combinations(nums)
#     for i in all_combinations:
#         if len(nums) == (2**len(i))-1:
#             return i
#
# numbers = [3,4,5,7,8,9,12]
#
# combinations = find_combination_to_target(numbers)
# print(combinations)
#
#
from itertools import combinations
a = [1,2,3,4,5]
answer = []
for i in range(1, len(a)-1):
    for j in list(combinations(a, i)):
        answer.append(sum(j))
answer = sorted(answer)
print(answer)