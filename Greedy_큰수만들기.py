# https://programmers.co.kr/learn/courses/30/lessons/42883
# def solution(number, K):
#     number = list(number)
#     k = len(number) - K
#     answer = []
#     answer.append(max(number[:-(k - 1)]))
#     k -= 1
#     while len(answer) != len(number)-K:
#         number = number[number.index(str(answer[-1:][0]))+1:]
#         if k == 1:
#             answer = answer + number[-1:]
#             break
#         answer.append(max(number[0:-(k-1)]))
#         k -= 1
#         if k == 1 :
#             answer = answer+number[-1:]
#             break
#     return ''.join(answer)

# 다른 사람 코드... 한참 부족하는걸 배운다..
def solution(number, k):
    s, sk = [], k
    for i, n in enumerate(number):
        while sk > 0 and s and s[-1] < n:
            print(s, sk)
            del s[-1]
            sk -= 1
        s.append(n)
        print(s)
    return ''.join(s[:len(number) - k])

if __name__ == "__main__":
    number = "4177252841"
    k = 4
    print(solution(number, k)) #775841