def solution(mylist):
    answer = ''
    for i in mylist:
        answer += i
    return answer

if __name__ == "__main__":
    mylist = ['1', '100', '33']
    print(solution(mylist))