# https://www.acmicpc.net/problem/2447
def star(n):
    if n == 3:
        return
    star(n//3)
    return
if __name__ == "__main__":
    n = 27
    print(star(n))