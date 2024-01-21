#https://www.acmicpc.net/problem/2309
data = []
for _ in range(9):
    data.append(int(input()))
data = sorted(data)
data_sum = sum(data) - 100
start = 0
end = len(data) - 1
answer = []
while start <= end:
    temp = data[start] + data[end]
    if temp > data_sum:
        end = end - 1
    elif temp < data_sum:
        start = start + 1
    else:
        answer.append(data[start])
        answer.append(data[end])
        break
for i in data:
    if i not in answer:
        print(i)
