def solution(array, commands):
    bask = []
    answer = []
    for i in range(len(commands)):
        x,y,z = commands[i]
        for arrays in range(x-1, y):
            bask.append(array[arrays])
            bask.sort()
        answer.append(bask[z-1])
        bask.clear()
    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))