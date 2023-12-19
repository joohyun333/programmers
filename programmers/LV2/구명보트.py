def solution(people, limit):
    port = [] # people인원들이 모였다가 limit 까지 차면 boat로 이동
    boat = [] # boat들
    people = sorted(people)
    people.reverse() # 순서 상관 없으므로 큰수부터 점검 (TC[90,80,70,30,20,10] ==> [70,10,20][90][80][30] 방지)

    # 구현 방식
    #people = [80,70,50,50] port로 people[0] 전달
    #port =[80] port가 limit(100)이 될때까지 people탐색, (100-80)>people은 없으므로 boat로 넘김
    #boat =[80]
    while people != []:
        if sum(port)+people[0] <= limit: #port + 옮겨갈 인원 합쳐서 limit  안 넘기면 people인원 옮김.
            port.append(people.pop(0))
            bask = [x for x in people if x <= (limit - sum(port))] # limit(100) - sum(port) = 20 보다 작은 people인원 착출.
            if bask != []: # 착출된 인원있으면, 무게가 무거운 인원부터 옮김. > people 큰수부터 정렬되있으므로, bask도 큰수 먼저 정렬됨.]
                port.append(bask[0])
                people.pop(people.index(port[-1]))
            else:
                pass
        else:
            boat.append(port[:]) #port + 옮겨갈 인원 합쳐서 limit 넘기면 기존에 있는 port에 있는 인원을 boat에 넘김.
            port.clear() # 보낸 port인원들은 삭제

        if people == []: # 마지막에 port에 남은인원들 boat로 마저 보냄. 끝.
            boat.append(port[:])
            port.clear()
    return  len(boat) # 근데 정확성 1,4,5 실패. 시간초과임. 이건 생각좀 해야겠다.

if __name__ == "__main__":
    people = [90,80,70,30,20,10,10]
    limit = 100
    print(solution(people,limit))