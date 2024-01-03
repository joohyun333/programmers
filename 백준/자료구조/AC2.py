# func_str = ""
# arr_length = 0
# test_case_count = int(input())
# for i in range(test_case_count):
#     func_str = input()
#     arr_length = [0, int(input())]
#     test_case = input().replace("[", "").replace("]","").split(",")
#
#     is_reverse = int('0',2)
#
#     for j in func_str:
#         if j == "R":
#             is_reverse = ~(int(str(is_reverse), 2))
#         elif j == "D":
#             if is_reverse == 0:
#                 arr_length[0] += 1
#             elif is_reverse == -1:
#                 arr_length[1] -= 1
#
#     if arr_length[0] > arr_length[1] :
#         print("error")
#         continue
#     test_case = test_case[arr_length[0]: arr_length[1]]
#     if is_reverse == -1:
#         test_case = list(reversed(test_case))
#     answer = "["
#     for j in test_case:
#         answer += j.replace("\'", "") + ","
#     answer = answer.strip(",") + "]"
#     print(answer)


if __name__ == "__main__" :
    p = bin(2)
    print(type(p))