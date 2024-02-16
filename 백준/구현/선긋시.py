data = []
for i in range(int(input())):
    s, e = map(int, input().split())
    data.append((s, e))
data.sort()
temp_s = -(10 ** 9) - 1
temp_e = -(10 ** 9) - 1
answer = 0
for i in range(len(data)):
    s, e = data[i]
    if temp_e < s:
        answer += abs(temp_e - temp_s)
        temp_s = s
        temp_e = e
    else:
        temp_e = max(e, temp_e)
print(answer + abs(temp_e - temp_s))
