#https://www.acmicpc.net/problem/10799
iron = input().split()
iron = iron[0].replace("()","1")
cnt = total = 0
for i in iron :
    if i == "(":
        cnt += 1
        total +=1
    elif i == "1":
        total+=cnt
    else:
        cnt-=1
print(total)