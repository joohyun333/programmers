def solution(n):
    print_list = ["수","박"]
    answer = ''
    for i in range(n):
        if i % 2 != 0 :
            answer += print_list[1]
        else:
            answer += print_list[0]
    return answer


if __name__ == "__main__":
    n = 3
    print(solution(n))