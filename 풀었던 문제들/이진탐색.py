line_num = int(input())
line = list(map(int, input().split()))
goal_number = int(input())

left = 0
right = line_num + 1
if goal_number in line:
    while left <= right:
        mid = (left + right) // 2
        if line[mid] == goal_number:
            print(mid + 1)
            break
        elif line[mid] > goal_number:
            right = mid - 1
            print(line[mid])
        elif line[mid] < goal_number:
            left = mid + 1
else:
    print("X")
