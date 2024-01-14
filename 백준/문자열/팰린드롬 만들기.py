# #https://www.acmicpc.net/problem/1213

data = sorted(list(input()))
arr = {}
for i in data:
    if arr.get(i):
        arr[i] += 1
    else:
        arr[i] = 1
answer = ["" for _ in range(len(data))]
start = 0
end = len(data)-1
for key in arr.keys():
    val = arr.get(key)
    while val > 1:
        if start <= end:
            answer[start] = key
            answer[end] = key
            arr[key] = val - 2
            val -= 2
            start += 1
            end -= 1
for i in arr:
    if arr.get(i) > 0 and answer.index("") != -1:
        idx = answer.index("")
        answer[idx] = i
        arr[i] -= 1
        break
is_answer = True
for i in arr:
    if arr.get(i) > 0:
        is_answer = False
        break
if is_answer:
    print(''.join(map(str, answer)))
else:
    print("I'm Sorry Hansoo")