import sys
input = sys.stdin.readline
N, M, V = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(M):
    num = int(input())
    if num < N:
        print(arr[num])
    else:
        print(arr[((num - V+1)%(N-V+1))+V-1])


# a = [int(input()) for i in range(M)]
# m_a = arr[:V-1]+arr[V-1:] * (max(a) // (N-V+1))
# for i in a:
#     print(m_a[i)]