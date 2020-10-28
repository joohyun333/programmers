from typing import List
from collections import Counter
def solution(clothes : List[str]) -> int:
    cloth = dict()
    cloth_num = 0
    for i, e in clothes:
        cloth.setdefault(e,[]).append(i)
    cloth_num = list(Counter(cloth.keys()).values())
    for i in range(cloth_num):
            
    return cloth_num, list(a)

if __name__ == "__main__":
    clothes = [["yellow_hat", "head"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    # clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))