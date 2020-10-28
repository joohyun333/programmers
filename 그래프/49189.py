def solution(n, edge):
    answer = [i for i in edge if i[0] == 1]

    return answer

if __name__ == "__main__":
    n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))