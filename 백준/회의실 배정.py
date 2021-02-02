# https://www.acmicpc.net/problem/1931
rooms = []
for i in range(int(input())):
    rooms.append(list(map(int, input().split())))
end_point= 0
result = 0
for start,end in sorted(rooms, key=lambda a:[a[1],a[0]]):
    if start >= end_point:
        end_point = end
        result += 1
print(result)
