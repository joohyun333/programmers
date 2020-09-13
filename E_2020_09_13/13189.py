def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        answer += mylist[i]
    return answer

if __name__ == "__main__":
    mylist = [['A', 'B'], ['X', 'Y'], ['1']]
    print(solution(mylist))