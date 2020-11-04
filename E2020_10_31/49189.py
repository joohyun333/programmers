from collections import defaultdict
def solution(n, edge):
    edge = sorted(edge)
    dic = defaultdict(list)
    for i,e in edge:
        dic[i].append(e)
        dic[e].append(i)
    #지나간 경로
    route = []
    # 경로 길이
    v = 0
    route_disteance = defaultdict(int)
    for i in range(1,n+1):
        for j in dic[i]:
            if j not in set(route):
                route.append(j)
    return dic, route_disteance, route

if __name__ == "__main__":
    n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))