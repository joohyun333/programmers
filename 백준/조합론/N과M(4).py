import itertools
N, M = map(int, input().split())
arr = map(int, input().split())
for i in itertools.permutations(sorted(arr), M):
    print(' '.join(map(str,list(i))))