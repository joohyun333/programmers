# https://www.acmicpc.net/problem/2098

def isIn(i, a):
    print(bin(i)[2:])
    print(bin(a)[2:])
    if a & (1 << (i - 2)) != 0:
        return True
    else:
        return False


print(isIn(8, 9))
