def solution(n):
    def Hanoi(s, e, d, n):
        if n <= 0:
            return
        Hanoi(s,d,e, n-1)
        result.append([s,d])
        Hanoi(e, s, d, n - 1)
    result = []
    Hanoi(1,2,3,n)  # [[1, 2], [1, 3], [2, 3]]
    return result
print(solution(2))