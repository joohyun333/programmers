import heapq
def solution(priorities, location):
    max_priorities = max(priorities)
    index = []
    for i in range(len(priorities)):
        index.append(i)

    answer = 0
    return answer

if __name__ == "__main__":
    a =list(map(int, input().replace("[","").replace("]","").split(",")))
    b = int(input())
    solution(a, b)