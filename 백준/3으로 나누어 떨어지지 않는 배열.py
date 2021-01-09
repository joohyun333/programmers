#https://www.acmicpc.net/problem/2938
import collections
N = int(input())
data = collections.deque(list(map(int, input().split())))
stack = []
while data:
    # data_N = len(data)
    v = data.popleft()
    if not stack:
        if data[0]+v % 3 != 0:
           stack.append(v)
           stack.append(data.popleft())
        else:
            data.append(v)
    elif stack[-1]+v % 3 != 0:
        stack.append(v)
    else:data.append(v)
    print(data, stack)

input()
a=[[],[],[]]
for v in map(int,input().split()):a[v%3]+=v,
if len(a[0])>1+len(a[1]+a[2])or (a[1] and a[2] and not a[0]):print(-1)
else:
 r=[]
 for v in a[0]:
  if r:r+=(a[1]or a[2]).pop(),
  r+=v,
 print(*a[1]+r+a[2])