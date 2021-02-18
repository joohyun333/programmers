N = int(input())
arr = [(1,0),(0,1)] #0,1
s= []
for i in range(N):
    n = int(input())
    s.append(n)
for j in range(2, max(s)+1):
    a,b = arr[j - 1],arr[j - 2]
    arr.append((a[0]+b[0],a[1]+b[1]))
for i in s:
    print(str(arr[i][0])+" "+str(arr[i][1]))