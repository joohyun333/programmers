import heapq
import copy
def solution(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m=a[0]
        i=1
        while m!=M:
            if m >= a[i]:
                m = a[i]
                answer+=1
            i+=1
        a.reverse()
    return answer
if __name__ == "__main__":
    a = [9,-1,-5]
    print(solution(a)) # 3
    # a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    # print(solution(a)) # 6
