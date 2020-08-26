
x = int(input())
y=""
while x>0:
    y=str(x%5)+y
    x//=5
print(y)
