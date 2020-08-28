# https://programmers.co.kr/learn/courses/30/lessons/67257
def solution(expression):
    sign_position = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]  # 우선순위
    sign = ["+", "-", "*"]
    number = []
    board = []
    for i in expression:
        if i in sign:
            board.append(''.join(number))
            board.append(i)
            number.clear()
        elif i not in sign:
            number.append(i)
    board.append(''.join(number))

    sign_position = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]  # 우선순위
    answer = []
    result = []
    position = 0
    for i in range(6):
        for j in range(3):
            if board in sign[i][j]:
                board.index()
    return board


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))