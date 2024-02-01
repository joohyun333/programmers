#https://www.acmicpc.net/problem/2800
import copy
from itertools import combinations
data = input()
stack = []
stack_col = []
answer = []
for idx, text in enumerate(data):
    if text == "(":
        stack.append((idx, 0))
    elif text == ")":
        i, s = stack.pop()
        stack_col.append((i, idx))
for i in range(1, len(stack_col)+1):
    perm = list(combinations(stack_col, i))
    for j in perm:
        data_str = copy.deepcopy(data)
        for z in j:
            start, end = z[0], z[1]
            data_str = data_str[:start] + "#" + data_str[start+1:]
            data_str = data_str[:end] + "#" + data_str[end+1:]
        data_str = data_str.replace("#", "")
        answer.append(data_str)
print('\n'.join(map(str, sorted(answer))))

