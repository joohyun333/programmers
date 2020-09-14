def solution(record):
    login = {}
    result = []
    for i in range(len(record)):
        if record[i].split(" ")[0] == "Enter" or record[i].split(" ")[0] == "Change":
            login[record[i].split(" ")[1]] = record[i].split(" ")[2]

    for i in range(len(record)):
        command = record[i].split(" ")
        if command[0] == "Enter":
            result.append(login[command[1]] + "님이 들어왔습니다.")
        elif command[0] == "Leave":
            result.append(login[command[1]] + "님이 나갔습니다.")
    return result


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))
