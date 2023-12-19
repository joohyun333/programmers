# https://programmers.co.kr/tryouts/17170/challenges
def solution(n:int) -> int:
    make_num = []
    while n>=3:
        a,b = divmod(n, 3)
        make_num.append(b)
        n = a
    make_num.append(n)
    print(make_num)
    answer = []
    for i, j in enumerate(make_num):
        answer.append(j*(3**(len(make_num)-i-1)))
    return sum(answer)

if __name__ == "__main__":
    # n = 45
    n = 100
    print(solution(n))