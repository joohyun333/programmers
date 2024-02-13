import sys, copy
from itertools import combinations

input = sys.stdin.readline
N, K = map(int, input().split())
alpha = [False for _ in range(26)]
alpha[0], alpha[2], alpha[8], alpha[13], alpha[19] = True, True, True, True, True
answer = 0
K = K - 5
remind = set()
remind_text = []
if K >= 0:
    for _ in range(N):
        t = input().strip('\n')
        t = t[4: len(t) - 4]
        if len(t) == 0:
            answer += 1
            N -= 1
        else:
            text = ''
            for i in t:
                if not alpha[ord(i) - 97]:
                    remind.add(ord(i) - 97)
                    text += i
            remind_text.append(text)
    max_answer = 0
    if len(remind) > K:
        for i in list(combinations(remind, K)):
            a = copy.deepcopy(alpha)
            temp_answer = 0
            for j in i:
                a[j] = True
            for j in remind_text:
                temp_len = len(j)
                for t in j:
                    if a[ord(t)-97]:
                        temp_len -= 1
                if temp_len == 0:
                    temp_answer += 1
            max_answer = max(max_answer, temp_answer)
        answer += max_answer
    else:
        answer += N
print(answer)
