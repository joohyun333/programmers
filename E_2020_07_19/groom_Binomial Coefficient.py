from functools import reduce
a, b = map(int, input().split())
numerator = [i for i in range(a, a-b, -1)] #분자리스트
denominator = [j for j in range(b,0,-1)] #분모리스트
for x1, x2 in enumerate(numerator):
    for y1, y2 in enumerate(denominator):
        if x2 % y2 == 0 :
            numerator[x1] = x2 // y2
            x2 = x2 // y2
            denominator[y1] = 1
        else:
            pass
num_muti = reduce(lambda x, y: x * y, numerator) // reduce(lambda x, y: x * y, denominator)
print(num_muti)