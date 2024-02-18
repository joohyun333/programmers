n, s = map(int, input().split())
data = list(map(int, input().split()))
sum_list = [0]
temp = 0
for i in range(n):
    temp += data[i]
    sum_list.append(temp)
start = 0
end = 0
answer = n+1
while start <= end < n+1:
    temp = sum_list[end] - sum_list[start]
    if temp >= s:
        answer = min(answer, end - start)
        start += 1
    else:
        end += 1

if answer == n+1:
    print(0)
else:
    print(answer)