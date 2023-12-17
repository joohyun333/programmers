# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    while trucks:
        answer += 1
        bridge_weight -= bridge.popleft()
        if bridge_weight + trucks[0] <= weight:
            t = trucks.popleft()
            bridge_weight += t
            bridge.append(t)
        else:
            bridge.append(0)
    answer += bridge_length
    return answer


if __name__ == "__main__":
    # bridge_length = 2
    # weight = 10
    # truck_weights = [7, 4, 5, 6]
    # print(solution(bridge_length, weight, truck_weights))
    # bridge_length = 100
    # weight = 100
    # truck_weights = [10]
    # print(solution(bridge_length, weight, truck_weights))
    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    print(solution(bridge_length, weight, truck_weights))
