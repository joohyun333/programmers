import sys
n = int(sys.stdin.readline())
list1 = []
for i in range(n):
    list1.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    list1[i][0], list1[i][1] = list1[i][1], list1[i][0]
list1.sort()
for i in range(n):
    list1[i][0], list1[i][1] = list1[i][1], list1[i][0]
    print(list1[i][0], list1[i][1])