from collections import defaultdict
from functools import reduce
from operator import mul
def solution(clothes):
    d = defaultdict(list)
    for i ,j  in clothes:
        d[j].append(i)
    nums = []
    for i in d.keys():
        nums.append(len(d[i])+1)
    answer = reduce(lambda x, y : mul(x, y), nums) -1
    return answer

if __name__ == "__main__" :
    a = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    # a = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
    print(solution(a))