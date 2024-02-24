n, m = map(int, input().split())
d = list(map(int, input().split()))
s, e = 1, (10 ** 9) + 1

while s < e:
    mid = (s + e) // 2
    count = 0
    temp = mid
    for i in d:
        if temp >= i:
            temp -= i
        else:
            if mid < i :
                if temp < mid:
                    count += 1
                temp = ((1 + (i // mid)) * mid) - i
                count += (i // mid) + 1
            else:
                temp = mid - i
                count += 1
    if temp < mid:
        count += 1
    if count <= m:
        e = mid
    else:
        s = mid + 1
print(s)
