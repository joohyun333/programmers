import collections
n, k = map(int, input().split())
num = collections.deque()
for i in range(1, n+1):
    num.append(i)
i = 1
result = []
while num:
    m = num.popleft()
    if i != k:
        num.append(m)
        i+=1
    else:
        result.append(m)
        i = 1
print("<"+', '.join(map(str, result))+">")