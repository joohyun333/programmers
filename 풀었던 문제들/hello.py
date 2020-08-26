# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
def solution(user_list):
    if user_list[0][0] == user_list[0][1]:
        return 0
    elif user_list[0][0] > user_list[0][1]:
        s = user_list[0][1]
        cost = user_list[1][-s] - user_list[1][0]
    return cost


if __name__ == "__main__":
    user_input = [[int(x) for x in input().split()] for y in range(2)]
    print(solution(user_input))

