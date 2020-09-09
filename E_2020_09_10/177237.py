import itertools as it
def solution(n):
    answer = []
    num = [i for i in range(1,n+1)]
    for i in range(1, n+1):
        for combination in it.combinations(num,i):
            if (combination[-1]-combination[0]) == len(combination)-1:
                if sum(combination) == n:
                    answer.append(combination)
    return len(answer)

if __name__ == "__main__":
    n = 15
    print(solution(n))
