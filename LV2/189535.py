# https://programmers.co.kr/skill_checks/189535
from typing import List
def solution(nums : List) -> int:
    num = set(nums)
    nums_len = len(nums)//2
    if len(num) < nums_len :
        return len(num)
    else:
        return nums_len

if __name__ == "__main__":
    nums =[1,2,3,4,5,6,7]
    # nums = [1,1,1,1,1]
    # nums = [1,2,1,1,1]
    print(solution(nums))