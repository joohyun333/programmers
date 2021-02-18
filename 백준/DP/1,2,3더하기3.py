import sys
input = sys.stdin.readline
T = int(input())
s = []
for i in range(T):
    s.append(int(input()))
arr = [1,2,4]
for i in range(3, max(s)):
    arr.append(((arr[i-3]+arr[i-2]+arr[i-1])%1000000009))
for i in s:
    print(arr[i-1]%1000000009)

