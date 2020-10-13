
# 우선순위가 높은 새끼만 뽑기
import random
from collections import defaultdict
def PQ(n, c):
    b = random.randint(0,4)
    c[b] = n
    return c, b

if __name__ == "__main__":
    c = defaultdict
    # while  in c :
    a = input()
    print(PQ(a, c))
