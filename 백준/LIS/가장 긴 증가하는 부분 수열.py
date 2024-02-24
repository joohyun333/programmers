N = int(input())
d = list(map(int, input().split()))
m = [1 for _ in range(N)]
for i in range(N):
    for j in range(0, i):
        if d[i] > d[j]:
            m[i] = max(m[j] + 1, m[i])
a = max(m)
answer = []
temp = a
for i in range(N-1, -1, -1):
    if m[i] == temp:
        temp -= 1
        answer.append(str(d[i]))
print(a)
answer.reverse()
print(' '.join(answer))
