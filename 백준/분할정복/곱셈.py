a, b, c = map(int, input().split())


def DC(a, b):
    if b == 1:
        return a % c
    else:
        n = DC(a, b // 2)
        if b % 2 == 0:
            return (n ** 2) % c
        elif b % 2 == 1:
            return ((n ** 2) * a) % c


print(DC(a, b))
