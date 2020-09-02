# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, K):
    number = list(number)
    k = len(number) - K
    answer = []
    answer.append(max(number[:-(k - 1)]))
    k -= 1
    while len(answer) != len(number)-K:
        number = number[number.index(str(answer[-1:][0]))+1:]
        if k == 1:
            answer = answer + number[-1:]
            break
        answer.append(max(number[0:-(k-1)]))
        k -= 1
        if k == 1 :
            answer = answer+number[-1:]
            break
    return ''.join(answer)

if __name__ == "__main__":
    number = "1924"
    k = 2
    print(solution(number, k)) #775841