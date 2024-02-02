from collections import deque
a, b = map(int, input().split())
max_num = max(a + 1, b + 1)
time_list = [-1 for _ in range(max(a + 2, b + 2))]
count = []
q = deque([[a,0]])

while q:
    idx, time = q.popleft()
    if idx == b:
        if time_list[idx] == -1 or time_list[idx] >= time:
            time_list[idx] = time
            count.append(time)
    if idx > max_num:
        break
    else:
        if time_list[idx] == -1 or time_list[idx] >= time:
            time_list[idx] = time
            for i in [idx - 1, idx + 1, idx * 2]:
                if 0 <= i <= max_num and (time_list[i] == -1 or time_list[i] >= time + 1):
                    q.append([i, time + 1])


print(time_list[b])
print(count.count(time_list[b]))
