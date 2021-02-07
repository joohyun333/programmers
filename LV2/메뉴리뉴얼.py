import collections
import itertools


def solution(orders, course):
    strs_counters = []
    max_counters = collections.defaultdict(lambda: 0)
    for i in orders:
        for z in range(1,len(i)+1):
            order = list(itertools.combinations(i, z))
            for j in order:
                j_strs = ''.join(sorted(j))
                strs_counters.append(j_strs)
    strs_counters = collections.Counter(strs_counters).most_common()
    answer = []
    for i,e in strs_counters:
        if len(i) in course and e>1 and e >= max_counters[len(i)]:
            max_counters[len(i)] = e
            answer.append(i)
    return sorted(answer)

if __name__ == "__main__":
    orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
    # ["AC", "ACDE", "BCFG", "CDE"]
    # orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
    # ["ACD", "AD", "ADE", "CD", "XYZ"]
    # orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]
    # ["WX", "XY"]
    print(solution(orders, course))
