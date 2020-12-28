# # https://www.acmicpc.net/problem/1082
# n = int(input())
# price = list(map(int, input().split()))
# money = int(input())
# card_price = sorted(list(zip(list(range(n)),price)), reverse=True) # [(3, 1), (2, 1), (1, 1), (0, 1)]
# best = min(card_price, key=lambda a:a[1]) # (3,1)
# card = [best[0] for i in range(money//best[1])]
# money-=len(card)*best[1]
# card_index = len(card)-1
# card_price.remove(best)
# while card_index>=0:
#     money += best[1]
#     for i, e in card_price:
#         if money >= e and i>card[card_index]:
#             money -= e
#             card[card_index] = i
#     if money==0:
#         break
#     card_index-=1
# print(int(''.join(map(str,reversed(card)))))
# =============================틀림===========
import sys
N = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())
S = ["" for i in range(51)]
for i in range(N):
    S[price[i]] = str(i)
def findMaximum(p:int):
    if S[p] == "":
        return
    for num in range(N):
        print(p,price[num], money)
        if p + price[num] > money:
            continue
        elif S[p + price[num]] == '':
            S[p + price[num]] = S[p] + str(num)
            continue
        elif int(S[p + price[num]]) >= int(S[p] + str(num)):
            continue
        S[p + price[num]] = S[p] + str(num)
    print(S)
for i in range(1, money + 1):
    print(i)
    findMaximum(i)
answer = 0
for i in range(money + 1):
    if S[i] == '':
        continue
    answer = max(answer, int(S[i]))
print(answer)

