from itertools import combinations
def solution(n, groups):
    lights = set(i+1 for i in range(n))
    lights_dum = [[i for i in range(groups[i][0],groups[i][1]+1)] for i in range(len(groups))]
    result = []
    result += lights_dum
    for i in range(len(lights_dum)):
        for j in range(i+1, len(lights_dum)):
            result.append(set(lights_dum[i] + lights_dum[j]))
    a = lights - max(result)

    return a, lights_dum, result

if __name__ == "__main__":
    n = 10
    groups = [[1, 5],[2, 7],[4, 8],[3, 6]]
    # n = 7
    # groups = [[6, 7],[1, 4],[2, 4]]
    # n =100
    # groups = [[1, 50],[1,100],[51, 100 ]]
    print(solution(n, groups))