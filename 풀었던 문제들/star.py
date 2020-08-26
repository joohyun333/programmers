# def concatenate(r1, r2):
#     return [''.join(x) for x in range(r1,r2,r1)]
#
# def star10(n):
#     if n == 1 :
#         return ['*']
#     n //= 3
#     x = star10(n)
#     top_bottom = concatenate(x, x)
#     middle = concatenate(x, [''*n]*n)
#     return top_bottom + middle + top_bottom
#
# print('\n'.join(star10(int(input()))))

arr = []
def make_star(N):
    for i in range(N):
        for j in range(N):
            arr.append("l")
        return arr
if __name__ == "__main__":
    print(make_star(int(input())))