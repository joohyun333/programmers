def solution(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x* y)
    return sum(result)

if __name__ == "__main__":
    a,b  = [1,2,3,4], [-3,-1,0,2]
    print(solution(a, b))
