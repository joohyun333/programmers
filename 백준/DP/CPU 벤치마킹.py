# # https://www.acmicpc.net/problem/20312
N = int(input())
cpus = list(map(int, input().split()))
result = 0
answer = 0
d = int(1e9)+7
for i in cpus:
    result*=i
    result+=i
    result%=d###########
    answer+=result
    answer%=d#########
print(answer)