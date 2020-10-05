# https://programmers.co.kr/learn/courses/30/lessons/42889
import timeit
import collections
def solution(N, stages):
    stage = collections.Counter(stages)
    result = collections.defaultdict(float)
    total_n = len(stages)
    for i in range(1,N+1):
        if total_n > 0 :
            result[i] = stage[i] / total_n
            total_n-=stage[i]
        else:
            result[i] = 0
    answer = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return [i for i,j in answer]

if __name__ == "__main__":
    a = timeit.default_timer()
    N, stage = 5, [2, 1, 2, 6, 2, 4, 3, 3]
    # N, stage = 4, [4,4,4,4,4]
    # N, stage = 8,[1,2,3,4,5,6,7]
    print(solution(N,stage))
    e = timeit.default_timer()
    print(e-a)