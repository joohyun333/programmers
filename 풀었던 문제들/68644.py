from itertools import combinations
def solution(numbers):
    return sorted(list(set([i+j for i,j in combinations(numbers, 2)])))

if __name__ == "__main__":
    numbers = [1,2,1,1]
    # numbers = [5,0,2,7]
    print(solution(numbers))