n = int(input())
data = list(input())
answer = -2**31


def dfs(idx, value):
    global answer
    if idx == n - 1:
        answer = max(answer, int(value))
        return
    else:
        if idx + 2 < n:
            case1 = eval(str(value) + data[idx + 1] + data[idx + 2])
            dfs(idx + 2, str(case1))
        if idx + 4 < n:
            case2 = eval(str(value) + data[idx + 1] + "(" + data[idx + 2] + data[idx + 3] + data[idx + 4] + ")")
            dfs(idx + 4, str(case2))


if n == 1:
    print(data[0])
else:
    dfs(0, data[0])
    print(answer)
