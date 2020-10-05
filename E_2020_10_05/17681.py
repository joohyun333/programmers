# https://programmers.co.kr/learn/courses/30/lessons/17681
import re
def solution(n, arr1, arr2):
    result, answer = [0]*n, []
    arr1 = [int(bin(i).lstrip('0b')) for i in arr1]
    arr2 = [int(bin(i).lstrip('0b')) for i in arr2]
    for i in range(n):
        result[i] = str(arr1[i] + arr2[i]).rjust(n,'0')
        answer.append(''.join(re.sub('[0]'," ",word) for word in re.sub('[1-2]',"#", result[i])))
    return answer

if __name__ == "__main__":
    # n = 5
    # arr1 , arr2 = [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
    n = 6
    arr1, arr2 = [27, 56, 19, 14, 14, 10], [46, 33, 33, 22, 31, 50]
    n = 6
    arr1, arr2 = [0, 0, 0, 10, 0, 0], [46, 33, 33, 22, 31, 50]
    print(solution(n, arr1, arr2))