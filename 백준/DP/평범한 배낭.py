# https://www.acmicpc.net/problem/12865
N, K = map(int, input().split())
thing = []
for i in range(N):
    thing.append(list(map(int, input().split())))
pack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = thing[i-1][0] # 무게
        v = thing[i-1][1] # 가치
        if w > j:
            pack[i][j] = pack[i - 1][j]
        else:
            pack[i][j] = max(v + pack[i - 1][j - w], pack[i - 1][j])
print(pack[N][K])


