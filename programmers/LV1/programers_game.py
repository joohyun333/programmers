# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
def solution(board, moves):
    basket = []
    result = 0
    for i in moves : #1 5 3 5 1 2 1 4
        for j in range(len(board)): # 0 1 2 3 4
            print(j, i-1)
            if board[j][i-1]:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    result += 2
                    del basket[-2:]
                break
    return result

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))
