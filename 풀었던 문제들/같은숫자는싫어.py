#https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i,e in enumerate(arr):
        if answer[-1] == e:
            pass
        else:
            answer.append(e)
    return answer

if __name__ == "__main__":
    arr = [4,4,4,3,3]
    print(solution(arr))