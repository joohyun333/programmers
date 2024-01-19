N, K = map(int, input().split())
A = list(map(int, input().split()))
sum_num = 0
for i in range(K):
    sum_num += A[i]
answer = sum_num
for j in range(K, N):
    sum_num += A[j]
    sum_num -= A[j-K]
    answer = max(answer, sum_num)
print(answer)