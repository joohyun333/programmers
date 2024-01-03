import sys

input = sys.stdin.readline


def solution(p, s, n):
    R_count = True
    D_count_front = 0
    D_count_end = 0
    for i in p:
        if i == "R":
            R_count = not R_count
        else:
            if R_count:
                D_count_front += 1
            else:
                D_count_end += 1
    if D_count_front + D_count_end <= n:
        result = s[D_count_front:n - D_count_end]
        if R_count:
            return "[" + ','.join(map(str, result)) + "]"
        else:
            return "[" + ','.join(map(str, result[::-1])) + "]"
    else:
        return "error" 


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        p = input().strip()
        n = int(input())
        s = eval(input())
        p = p.replace("RR", "")
        print(solution(p, s, n))
