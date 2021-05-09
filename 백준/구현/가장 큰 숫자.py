# https://www.acmicpc.net/problem/16458
import collections, sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input()[:-1] for _ in range(n)]
discoverd = [[False] * m for _ in range(n)]

num_DP = collections.defaultdict(list)
num_DP[0] = [['*', '*', '*'], ['*', ' ', '*'], ['*', ' ', '*'], ['*', ' ', '*'], ['*', '*', '*']]
num_DP[1] = [['*', '*', ' '], [' ', '*', ' '], [' ', '*', ' '], [' ', '*', ' '], ['*', '*', '*']]
num_DP[2] = [['*', '*', ' '], [' ', ' ', '*'], [' ', '*', ' '], ['*', ' ', ' '], ['*', '*', '*']]
num_DP[3] = [['*', '*', '*'], [' ', ' ', '*'], [' ', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']]
num_DP[4] = [[' ', ' ', '*'], [' ', '*', '*'], ['*', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*']]
num_DP[5] = [['*', '*', '*'], ['*', ' ', ' '], ['*', '*', ' '], [' ', ' ', '*'], ['*', '*', '*']]
num_DP[6] = [['*', ' ', ' '], ['*', ' ', ' '], ['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
num_DP[7] = [['*', '*', '*'], [' ', ' ', '*'], [' ', '*', ' '], ['*', ' ', ' '], ['*', ' ', ' ']]
num_DP[8] = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
num_DP[9] = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], [' ', ' ', '*']]


def boolean_number(i, j):
    global discoverd
    queue = collections.deque([[i, j]])
    discoverd[i][j] = True
    num_result = [[" "] * m for _ in range(n)]
    distance = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
    min_y, min_x = sys.maxsize, sys.maxsize
    max_y, max_x = 0, 0
    while queue:
        y, x = queue.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        num_result[y][x] = "*"
        for dy, dx in distance:
            if 0 <= y + dy < n and 0 <= x + dx < m and arr[y + dy][x + dx] == "*" and not discoverd[y + dy][x + dx]:
                discoverd[y + dy][x + dx] = True
                queue.append([y + dy, x + dx])
    multiple = (max_x - min_x + 1) // 3
    total = []
    for nums in num_result[min_y: max_y + 1][::multiple]:
        total.append(nums[min_x:max_x + 1][::multiple])
    answer = 0
    for d in num_DP:
        if num_DP[d] == total:
            answer = d
    return multiple, answer


size = 0
num_result = 0
for i in range(n):
    for j in range(m):
        if not discoverd[i][j] and arr[i][j] == "*":
            multi, num = boolean_number(i, j)
            if multi > size:
                size = multi
                num_result = num
print(num_result)