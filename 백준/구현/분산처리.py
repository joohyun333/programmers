# import sys
#
# def repeated_squaring(denominator, exponent):
#     if denominator % 10 == 0:
#         return 10
#     else:
#         return pow(denominator, exponent, 10)
# if __name__ == '__main__':
#     for _ in range(int(sys.stdin.readline())):
#         d, e = tuple(map(int, sys.stdin.readline().split()))
#         print(repeated_squaring(d, e))
for l in [*open(0)][1:]:
    print(10+pow(*map(int,l.split()),-10))