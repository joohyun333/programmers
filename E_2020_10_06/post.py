def solution(data1, name):
    person = data1.split("#")
    income = {}
    for i in person:
        income[i.split(" ")[0]] = sum([int(i) for i in i.split(" ")[1].split(",")])
    return income[name]

if __name__ == "__main__":
    name = 'Jack'
    data1 = 'Jack 12,3,4,5#Bob 1234#Power 322,121,33'
    print(solution(data1, name))