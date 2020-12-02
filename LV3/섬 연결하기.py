#https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3
def solution(n, costs):
    costs = [i for i in costs if len(i) > 2]
    costs.sort(key=lambda x : x[2], reverse=True)
    answer = [0] * n
    total_cost = sum([i[2] for i in costs])
    for i in costs:
        answer[i[0]] += 1
        answer[i[1]] += 1
    while 0 not in answer and sum(answer) > (n-1)*2:
        a, b, c = costs.pop(0)
        if answer[a] > 1 and answer[b]>1:
            answer[a] -= 1
            answer[b] -= 1
            total_cost -= c
    return total_cost
if __name__ == "__main__":
    # n, costs = 5, [[0,1,5],[1,2],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
    n, costs =  5 ,[[0,1,1],[3,4],[1,2,2],[2,3,4]]
    print(solution(n, costs))