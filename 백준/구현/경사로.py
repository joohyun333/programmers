import sys

input = sys.stdin.readline
N, L = map(int, input().split())
data = []


def find(list_, visited):
    for j in range(len(list_) - 1):
        if list_[j] > list_[j + 1]:
            if j + L < len(list_):
                status = [list_[num] for num in range(j, j + L + 1)]
                visited_status = set([visited[num] for num in range(j+1, j + L + 1)])
                case = [list_[j]] + [list_[j] - 1] * L
                if (status == case) and visited_status == {False}:
                    for num in range(j+1, j + L + 1):
                        visited[num] = True
                else:
                    return False, visited
            else:
                return False, visited
    return True, visited


for _ in range(N):
    d = list(map(int, input().split()))
    data.append(d)
answer = 0
for i in range(N):
    list_1 = data[i]
    list_2 = []
    for j in range(N):
        list_2.append(data[j][i])

    discovered = [False] * N
    result1, new_discovered = find(list_1, discovered)
    result2, new_discovered = find(list_1[::-1], new_discovered[::-1])
    if result1 and result2:
        answer += 1

    discovered = [False] * N
    result1, new_discovered = find(list_2, discovered)
    result2, new_discovered = find(list_2[::-1], new_discovered[::-1])
    if result1 and result2:
        answer += 1
print(answer)
