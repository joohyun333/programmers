def solution(number, k):
    front = number[:-k+1]
    back = number[-k+1:]
    answer = ''
    front_max = front.count(str(max(front)))
    for i in range(len(number)-k-len(back)):
        if front_max >= 1:
            answer += max(front) * front_max
            front = front.replace(str(max(front)), "1")

    answer += back
    return answer

if __name__ == "__main__":
    number = "4177252841"
    k = 4
    print(solution(number, k))