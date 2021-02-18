T = int(input())
arr = [1,2,4]
for i in range(3, 11):
    arr.append(sum(arr[i-3:i]))
for i in range(T):
    a = int(input())
    print(arr[a-1])