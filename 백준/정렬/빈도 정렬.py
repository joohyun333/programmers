# https://www.acmicpc.net/problem/2910
N, C = map(int, input().split())
data_dic = {}
d = list(map(int, input().split()))
for idx, val in enumerate(d):
    if val not in data_dic:
        data_dic[val] = [-1, idx + 1]
    else:
        d_key = data_dic[val]
        d_key[0] = d_key[0] - 1
        data_dic[val] = d_key
data_dic = sorted(data_dic.items(), key=lambda x: (x[1][0], x[1][1]))
answer = []
for i in data_dic:
    for _ in range(i[1][0], 0):
        answer.append(i[0])
print(' '.join(map(str, answer)))