#https://www.acmicpc.net/problem/9012
N = int(input())
data = []
for i in range(N):
    data.append(input())
def remove(s):
    dix = len(s)//2
    for _ in range(dix):
        if "()" in s:
            s = s.replace("()","")
    if s:
        return "NO"
    else:
        return "YES"
for i in data:
    print(remove(i))