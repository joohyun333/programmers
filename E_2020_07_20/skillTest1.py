def solution(num):
    i = 0
    while num != 1:
        if num % 2 == 0 :
            num = num // 2
            i += 1
            print(i)
            if i == 500 :
                return -1
                break
        else:
            num = (num*3)+1
            i += 1
            print(i)
            if i == 500 :
                return -1
                break
    return i

if __name__ == "__main__":
    a = int(input())
    print(solution(a))