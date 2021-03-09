def back_tracking(idx):
    for i in range(1, (idx // 2) + 1):
        if s[-i:] == s[-2 * i:-i]: return -1
    if idx == n:
        print(''.join(map(str, s)))
        return 0
    for i in range(1, 4):
        s.append(i)
        print(i)
        if back_tracking(idx + 1) == 0:
            return 0
        s.pop()
if __name__ == "__main__":
    n = int(input())
    s = []
    back_tracking(0)
