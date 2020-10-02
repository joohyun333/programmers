# https://level.goorm.io/exam/58258/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%9E%88%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-9%EC%B0%A8/quiz/1
corn= list(map(int,input().split()))
day =int(input())
patten = [1,0]
for i in range(day):
    if patten[0] == 1:
        if corn[0] % 2 == 0:
            corn[1] = corn[1]+corn[0]//2
            corn[0] = corn[0]//2
        else:
            corn[1] = corn[1] + corn[0] // 2 + 1
            corn[0] = (corn[0] // 2)
        patten[0] = 0
        patten[1] = 1
    elif patten[1] == 1:
        if corn[1] % 2 == 0:
            corn[0] = corn[0]+corn[1]//2
            corn[1] = corn[1]//2
        else:
            corn[0] = corn[0] + corn[1] // 2 + 1
            corn[1] = (corn[1] // 2)
        patten[1] = 0
        patten[0] = 1
print(corn[0], corn[1])
