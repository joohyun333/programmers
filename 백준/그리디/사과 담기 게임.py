# https://www.acmicpc.net/problem/2828
N, M = map(int, input().split())
space = [0, M-1]
answer = 0
for i in range(int(input())):
    data = int(input()) - 1
    distance = 0
    if space[0] <= data <= space[1]:
        pass
    elif space[1] < data:
        distance = data - space[1]
        space = [space[0] + distance, space[1] + distance]
        answer += distance
    else:
        distance = space[0] - data
        space = [space[0] - distance, space[1] - distance]
        answer += distance
print(answer)