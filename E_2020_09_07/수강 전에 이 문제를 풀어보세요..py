# def solution(mylist):
#     answer = []
#     for i in mylist:
#         answer.append(len(i))
#     return answer
# 사실 이 코드는 python이 아닌 java나 c에 가깝다고 한다....

def solution(mylist):
    return list(map(len, mylist))
# 이렇게 짜는것을 목표로 하자

if __name__== "__main__":
    input = [[1], [2]]
    print(solution(input))