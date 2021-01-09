# https://www.acmicpc.net/problem/17609
N = int(input())
s = []
for _ in range(N):
    s.append(input())
def palindrome(s):
    if s == s[::-1]:
        return 0
    for n in range(len(s)):
        s_=s[:n]+s[n+1:]
        print(s_)
        if s_ == s_[::-1]:
            return 1
    return 2
for i in s:
    print(palindrome(i))