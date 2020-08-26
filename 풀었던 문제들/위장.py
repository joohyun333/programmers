from collections import defaultdict
def solution(clothes):
    d = defaultdict(list)
    num = 1
    for i ,j  in clothes:
        d[j].append(i)

    for i in d.keys():
        a = len(d[i])
        print(a)
        num *= len(d[i])+1
    return num-1

if __name__ == "__main__" :
    a = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    print(solution(a))