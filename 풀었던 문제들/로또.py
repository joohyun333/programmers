from itertools import combinations
while True:
    line = list(map(int, input().strip().split()))
    n = line[0]
    if n == 0:
        break
    for balls in combinations(line[1:], 6):
        print(' '.join(map(str, balls)))
    print('')