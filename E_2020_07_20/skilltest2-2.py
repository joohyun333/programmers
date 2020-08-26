
def solution(io):
    io2 =[[]]
    for i in io:
        if i not in io2:
            io2.append(i)
        elif i in io2:
            pass
    result = len(io2)-1
    return result
if __name__ == "__main__":
    io = [[1, 1], [2, 1], [1, 2], [3, 4], [2, 1], [2, 1]]
    io1  = [[1,1],[2,2],[3,3]]
    print(solution(io))
    print(solution(io1))