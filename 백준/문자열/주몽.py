#https://www.acmicpc.net/problem/1940
N = int(input())
M = int(input())
data = sorted(list(map(int, input().split())))
start = 0
end = N-1
answer = 0
while start < end:
    s = data[start] + data[end]
    if s < M:
        start += 1
    elif s > M:
        end -= 1
    else:
        answer += 1
        start += 1
        end -= 1
print(answer)