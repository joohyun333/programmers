# https://www.acmicpc.net/problem/1157
import collections
n = input().lower()
n_dic = collections.Counter(n)
if list(n_dic.values()).count(max(n_dic.values())) > 1:
    print("?")
else:
    result = n_dic.most_common(1)[0][0]
    print(str(result).upper())