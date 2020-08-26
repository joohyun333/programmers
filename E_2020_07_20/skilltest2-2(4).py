from collections import deque
def solution(people, limit):
    people = people
    p=[]
    for i in range(len(people)):
        p.append([(people[i], peoples) for peoples in people[i+1:] if (limit - people[i]) >= peoples])
        if people[i] > limit//2:
            p.append(people[i])
    return len(p)//2

if __name__ == "__main__":
    people = [70, 50, 80]
    limit = 100
    print(solution(people,limit))