num, base = map(int, input().strip().split(' '))
num = str(num)
result = 0
for i, e in enumerate(num):
    result += int(e) * (base**(len(num)-(i+1)))
print(result)