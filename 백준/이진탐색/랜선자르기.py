import sys
input = sys.stdin.readline
K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))
start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2
    total = sum([i//mid for i in arr])
    if total>=N:
        start = mid+1
    else:
        end = mid-1
print(end)