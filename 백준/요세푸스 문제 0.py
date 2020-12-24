# https://www.acmicpc.net/problem/11866
import collections
n, k  = map(int, input().split())
m = collections.deque(list(range(1,n+1)))
count = 1
discard = 0
result = []
while m:
    if count < k:
        count+=1
        m.append(m.popleft())
    else:
        count=1
        result.append(m.popleft())
print("<"+', '.join(map(str,result))+">")
