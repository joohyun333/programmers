import re
from typing import List
def solution(n : int , delivery: List[int]) -> str:
    result = [0]*n
    for x, y, z in delivery:
        if z == 1:
            result[x-1] = "O"
            result[y-1] = "O"
    for x, y, z in delivery:
        if result[x-1] =="O" and z == 0:
            result[y-1] = "X"
        elif result[y-1] =="O" and z == 0:
            result[x-1] = "X"
    answer = "".join(map(str, result))
    answer = re.sub("0", "?", answer)
    return answer

if __name__ == "__main__":
    # n, delivery = 6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]
    n, delivery = 7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]
    print(solution(n, delivery))