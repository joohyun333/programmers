import collections
N = int(input())
s = input()
start = 2
end = len(s)
answer = 0
while start <= end:
    count = []
    mid = (start+end)//2
    new_str = collections.deque(s[:mid])
    count.append(''.join(list(new_str)))
    for i in s[mid:]:
        str_popleft = new_str.popleft()
        new_str.append(i)
        count.append(''.join(list(new_str)))
    count_max = collections.Counter(count).most_common(1)[0]
    count.clear()
    max_str, max_num = count_max[0], count_max[1]
    del count_max
    if max_num >= 2 and max_num>answer:
        answer = max_num
    if answer == 0:
        end = mid-1
    elif answer>0:
        start = mid+1
print(answer)