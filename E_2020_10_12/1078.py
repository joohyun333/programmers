# https://www.acmicpc.net/problem/1078
def solution(n):
    s = 0
    s_i = 0
    while s - s_i != n :
        s += 1
        s_i = int(''.join(reversed(list(str(s)))))
        if s >= 10000000:
            return -1
    else: return s

if __name__ == "__main__":
    print(solution(int(input())))
