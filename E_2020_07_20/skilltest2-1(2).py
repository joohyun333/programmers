import numpy as np
def solution(arr1, arr2):
    arr = [[0 for _ in range(len(arr1))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr = arr1[i][j] * arr2[i][j]
    return arr
if __name__ == "__main__":
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    print(solution(arr1, arr2))