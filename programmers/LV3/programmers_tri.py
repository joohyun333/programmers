# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
                # 0열 모두 더하고
            elif i == j:
                triangle[i][j] += triangle[i-1][j-1]
                # 마지막 줄 모두 더하고
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                # 겹치는 값중에 큰것만 고르면 답나옴.
    return max(triangle[len(triangle)-1])

if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))