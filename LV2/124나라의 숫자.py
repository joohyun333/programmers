# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    T = "124"
    if n <= 3:
        return T[n-1]
    else:
        p, r = divmod(n-1, 3)
        return solution(p) + T[r]

if __name__ == "__main__":
    print(solution(input()))