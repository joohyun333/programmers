from collections import deque


# 주식 가격이 떨어 지지 않은 기간은 몇 초인지 구하는 문제

def solution(prices):
    answer = [0] * len(prices)
    stack = deque([(0, 0)])
    price = list(zip([i for i in range(len(prices))], prices))
    for i in range(1, len(prices)):
        while stack and price[i][1] < price[stack[-1][0]][1]:  # 주식 가격이 떨어질 때
            s = stack.pop()
            answer[s[0]] = price[i][0] - s[0]  # 이전 가격의 기간을 계산 한다.
        stack.append(price[i])
    while stack: # 나머지는 주식 가격이 계속 오른 경우
        s = stack.pop()
        answer[s[0]] = len(price) - 1 - s[0]
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]  # [4, 3, 1, 1, 0]
    print(solution(prices))
