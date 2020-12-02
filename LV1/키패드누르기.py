# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = []
    position = [[3,0],[3,2]]  #왼손포지션 * / 오른손 포지션 # default
    board = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] #키패드
    for x in numbers:
        if x in [1,4,7]:
            answer.append("L")
            position[0] = board[x]
        elif x in [3,6,9]:
            answer.append("R")
            position[1] = board[x]
        else:
            distance_left = abs(board[x][0]-position[0][0]) + abs(board[x][1]-position[0][1]) # 왼손으로부터 다음 number까지 거리
            distance_right = abs(board[x][0]-position[1][0]) + abs(board[x][1]-position[1][1]) # 오른손으로부터 다음 number까지 거리
            if distance_left < distance_right:
                answer.append("L")
                position[0] = board[x]
            elif distance_right < distance_left :
                answer.append("R")
                position[1] = board[x]
            else:
                if hand == "right" :
                    answer.append("R")
                    position[1] = board[x]
                else:
                    answer.append("L")
                    position[0] = board[x]
    return ''.join(answer)

if __name__ == "__main__" :
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))