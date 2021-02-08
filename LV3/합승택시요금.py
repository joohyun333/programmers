# https://programmers.co.kr/learn/courses/30/lessons/72413
import collections
import heapq
def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    for start, dis, fee in fares:
        graph[start].append((dis, fee))
        graph[dis].append((start, fee))

    def Dijkstra(s, d):
        queue = [(0, s)]
        discoverd = [False] * (n + 1)
        dis = collections.defaultdict(list)
        while queue:
            node_fee, node = heapq.heappop(queue)
            if node == d:
                dis[node] = node_fee
                return dis
            elif node != d and discoverd[node] == False:
                discoverd[node] = True
                dis[node] = node_fee
                for i, fee in graph[node]:
                    new_fee = fee + node_fee
                    heapq.heappush(queue, (new_fee, i))
        return dis

    mid_Dijkstra = Dijkstra(s, n + 1)
    mid = collections.deque(mid_Dijkstra.items())
    min_fees = mid_Dijkstra[a] + mid_Dijkstra[b]
    mid.popleft()
    for i, e in mid:
        a_ = Dijkstra(i, a)[a]
        b_ = Dijkstra(i, b)[b]
        m = e+a_+b_
        if m < min_fees: min_fees=m
    return min_fees


if __name__ == "__main__":
    n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66],
                                     [2, 3, 22], [1, 6, 25]]# 82
    n, s, a, b, fares = 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]] # 14
    # n, s, a, b, fares = 6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8],
    #                                  [4, 3, 9]]# 18
    print(solution(n, s, a, b, fares))
