import math
import collections
import bisect

nums = []
while True:
    N = int(input())
    if not N:
        break
    nums.append(N)

# 에라토스테네스의 체
n = max(nums)

def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True] # max nums까지 소수 출력
num = prime_list(n)
num.pop(0)
result = collections.defaultdict()
for a in nums:
    for i in num:
        search = bisect.bisect_left(num, a - i)
        if search<len(num) and num[search] == a - i:
            result[a] = (i, num[search])
            break
for i in nums:
    if i in result:
        print(str(i) + " = " + str(result[i][0]) + " + " + str(result[i][1]))
    else:
        print("Goldbach's conjecture is wrong.")
