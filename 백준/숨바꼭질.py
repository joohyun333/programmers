# https://www.acmicpc.net/problem/1697
a, b = map(int, input().split())
queue = [(a,0)]
discoverd = [False]*100001
while queue:
    v = queue.pop(0)
    dis = v[0]
    count = v[1]
    if not discoverd[dis]:
        discoverd[dis] = True
        if dis == b:
            print(count)
            break
        count+=1
        if dis-1 >= 0:
            queue.append((dis-1, count))
        if dis+1 <= 100000:
            queue.append((dis + 1, count))
        if dis*2 <= 100000:
            queue.append((dis * 2, count))
