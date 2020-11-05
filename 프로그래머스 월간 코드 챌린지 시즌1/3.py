from itertools import combinations_with_replacement
def starsequence(n):
    if len(n)<2 or len(n)%2 == 1:
        return 0
    num = [n[0], n[1]]
    for i in range(0,len(n), 2):
        if len(set([n[i], n[i+1]]) - set(num))<=1 and n[i] != n[i+1]:
            pass
        else:
            return 0
    return len(n)

def solution(s):
    res = [[]]
    max_num = 0
    for num in s:
        res += [item + [num] for item in res if (item + [num] not in res and (len(item) == 0 or item[-1] <= num))]
    return [values for values in res if len(values) > 1]

if __name__ == "__main__":
    s = [5,2,3,3,5,3]
    # s = [0,3,3,0,7,2,0,2,2,0]
    # s = [1,2,3,4,5]
    # print(starsequence(s))
    print(solution(s))