# https://www.acmicpc.net/problem/4375
from builtins import EOFError

while True:
    try:
        n = int(input())
    except EOFError:
        break
    answer = 1
    while True:
        if int(answer) % n == 0 :
            print(len(str(answer)))
            break
        else:
            answer = (answer * 10) +1
