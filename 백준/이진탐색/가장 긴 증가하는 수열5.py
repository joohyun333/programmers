# https://www.acmicpc.net/problem/12015
import sys, bisect

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
result = [-sys.maxsize]
change = []

for i in arr:
    if result[-1] < i:
        result.append(i)
    else:
        a = bisect.bisect_left(result, i)
        change.append((result[a], i, a))  # 기존, 바꿀
        result[a] = i
result = result+[sys.maxsize]

for first, end, index in reversed(change):
    left, right = False, False
    if result[index - 1] < first:
            left = True
    if result[index + 1] > first:
            right = True
    if left and right:
        result[index] = first

print(len(result)-2)
print(' '.join(map(str, result[1:-1])))
