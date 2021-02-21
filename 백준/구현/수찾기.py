N = int(input())
N_data = sorted(list(map(int, input().split())))
M = int(input())
M_data = list(map(int, input().split()))
def binary_search(m):
    start = 0
    end = N-1
    while start<=end:
        mid = (start+end)//2
        if N_data[mid] == m:
            return 1
        elif N_data[mid] < m:
            start = mid+1
        else:
            end = mid - 1
    return 0
for i in M_data:
    print(binary_search(i))