import sys
input = sys.stdin.readline
n = int(input())
white, blue = 0,0
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
result = []
b, w = 0,0
def solution(paper):
    N = len(paper)
    if set(sum(paper,[])) == {0}:
        result.append("W")
        return
    elif set(sum(paper,[]))== {1}:
        result.append("B")
        return
    solution([i[0:N//2] for i in paper[0:N//2]])
    solution([i[N // 2:N+1] for i in paper[0:N // 2]])
    solution([i[0:N // 2] for i in paper[N // 2:N+1]])
    solution([i[N // 2:N+1] for i in paper[N // 2:N+1]])
solution(p)
print(result.count("W"))
print(result.count("B"))