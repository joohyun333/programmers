A, B = map(int, input().split())
C = B
coin_list=[int(input()) for _ in range(A)]
coin_list.reverse()
R = 0
for i in range(A):
    if B // coin_list[i] >= 1:
        R += B // coin_list[i]
        B = B % coin_list[i]
print(R)

R=0
for i,coins in enumerate(coin_list):
    temp = C // coins
    R = R + temp
    C = C - temp * coins
print(R)
