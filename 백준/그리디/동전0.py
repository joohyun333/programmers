A, B = map(int, input().split())
coin_list=[int(input()) for _ in range(A)]
coin_list.reverse()
R = 0
for i in range(A):
    if B // coin_list[i] >= 1:
        R += B // coin_list[i]
        B = B % coin_list[i]

print(R)
