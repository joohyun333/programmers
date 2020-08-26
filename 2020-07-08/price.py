import heapq
def solution(prices):
    heap = []
    answer = []
    for i in len(prices):
        heapq.heappush(heap, prices[i])
        if heap[i] > heap[i:]:
            heapq.heappop(heap, heap[i])
            answer.append(len(heap))

    return answer, heap

if __name__ == "__main__" :
    a = input().replace("[","").replace("]","").split(",")
    a = list(map(int, a)) #[1, 2, 3, 2, 3]
    solution(a)