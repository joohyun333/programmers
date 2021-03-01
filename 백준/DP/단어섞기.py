import sys

input = sys.stdin.readline
N = int(input())
for n in range(1, N + 1):
    a, b, c = map(str, input().split())
    a_len, b_len, c_len = len(a), len(b), len(c)
    arr = [[0] * (b_len + 1) for i in range(a_len + 1)]
    arr[0][0] = True
    for i in range(1, a_len + 1):
        if a[i - 1] == c[i - 1]:
            arr[i][0] = arr[i - 1][0]
        else:
            arr[i][0] = False

    for i in range(1, b_len + 1):
        if b[i - 1] == c[i - 1]:
            arr[0][i] = arr[0][i - 1]
        else:
            arr[0][i] = False

    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            a_str, b_str, c_str = a[i - 1], b[j - 1], c[i + j - 1]
            if a_str == c_str and b_str == c_str:
                arr[i][j] = arr[i - 1][j] | arr[i][j - 1]
            elif a_str == c_str and b_str != c_str:
                arr[i][j] = arr[i - 1][j]
            elif a_str != c_str and b_str == c_str:
                arr[i][j] = arr[i][j - 1]
            else:
                arr[i][j] = False

    if arr[a_len][b_len] == True:
        print("Data set %s: yes" % str(n))
    else:
        print("Data set %s: no" % str(n))

