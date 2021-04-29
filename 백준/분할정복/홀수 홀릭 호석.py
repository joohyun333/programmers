# https://www.acmicpc.net/problem/20164
import itertools, sys

input = sys.stdin.readline
N = list(map(str, input().strip()))
result = []


def count(n:str):
    return len([i for i in n if int(i) % 2 == 1])


def divide(n, counts):
    if len(n) == 1:
        return result.append(counts)
    elif len(n) == 2:
        sum_n = sum([int(i) for i in n])
        divide(list(str(sum_n)), counts + count(str(sum_n)))
    elif len(n) > 2:
        for i, j in list(itertools.combinations(range(1, len(n)), 2)):
            divide_list = int(''.join(n[0:i])) + int(''.join(n[i:j])) + int(''.join(n[j:len(n)]))
            divide(list(str(divide_list)), counts+count(str(divide_list)))

divide(N, count(N))
print(min(result), max(result))