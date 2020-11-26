from itertools import combinations
def solution(data):
    result = 0
    col_cnt = len(data[0])
    lst = list(range(0, col_cnt))
    c_lst = []
    final = []

    for i in range(1, col_cnt + 1):
        c = combinations(lst, i)
        c_lst.extend(c)

    # 유일성 만족하는 조합 찾기
    for i in c_lst:
        final_tmp = []
        for row in range(0, len(data)):
            tmp_lst = []
            for t in i:
                tmp_lst.append(data[row][t])
            final_tmp.append(tuple(tmp_lst))
        # check (컬럼 조합한 값에서 중복이 없어야 유일성 만족)
        if len(set(final_tmp)) == len(data):
            final.append(i)

    # 최소성 만족하는 조합 골라내기
    print(final)
    final_set = set(final)
    for i in range(0, len(final) - 1):
        for j in range(i + 1, len(final)):
            # 최소성을 만족하지 못한 경우
            if set(final[i]) == set(final[i]) & set(final[j]):
                final_set.discard(final[j])

    result = len(final_set)

    return result
if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    # relation = [["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"],["1","2","3"]]
    # # relation = [["11"],["111"]]
    print(solution(relation))