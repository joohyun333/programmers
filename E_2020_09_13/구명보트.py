def solution(people, limit):
    port = [] # limit 채우는 공간
    boat = [] # port에서 limit 까지 채운 인원들 채움.
    people = sorted(people)
    people.reverse()
    while people != []:
        if sum(port)+people[0] <= limit:
            port.append(people.pop(0))
            bask = [x for x in people if x <= (limit - sum(port))]
            if bask != []:
                port.append(bask[0])
                people.pop(people.index(port[-1]))
            else:
                pass
        else:
            boat.append(port[:])
            port.clear()

        if people == []:
            boat.append(port[:])
            port.clear()
    return  len(boat)

if __name__ == "__main__":
    people = [40,40,40]
    limit = 100
    print(solution(people,limit))