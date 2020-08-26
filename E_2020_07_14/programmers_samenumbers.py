def solution(arr):
    # answer = []
    for i in range(1,len(arr)):
        if arr[0] == arr[i]:
            arr.pop(1)
            print(arr)
    #     else:
    # #         answer.append(arr.pop(0))
    # return answer


if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    print(solution(arr))