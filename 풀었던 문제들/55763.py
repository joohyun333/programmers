#https://programmers.co.kr/learn/courses/9877/lessons/55763
def solution(n, lost, reserve):
    lost_del = set(lost)-set(reserve)
    reserve_del = set(reserve)-set(lost)
    for i in reserve_del:
       if i-1 in lost_del:
           lost_del.remove(i-1)
       elif i+1 in lost_del:
           lost_del.lost_del(i+1)
    return n-len(lost_del)

if __name__ == "__main__":
    # n, lost, reserve = 5, [2,4], [1,3,5]
    # n, lost, reserve = 5, [2, 4], [3]
    # n, lost, reserve = 3, [3], [1]
    n, lost, reserve = 5, [4], [5]
    print(solution(n, lost, reserve))