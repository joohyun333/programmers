import sys
import collections
input = sys.stdin.readline
node = [False] *(int(input())+1)
start, end = map(int, input().split())
arr = collections.defaultdict(list)
for i in range(int(input())):
    parent, descendants = map(int, input().split())
    arr[parent].append(descendants)
    arr[descendants].append(parent)
c = 0
def dfs(s, e, count):
    global c
    if s == e :
        c = count
        return
    for i in arr[s]:
        if not node[i]:
            node[i] =True
            dfs(i, e, count+1)
dfs(start, end, 0)
if c>0:
    print(c)
else:
    print("-1")