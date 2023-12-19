def solution(n, times):
    first = 1
    end = n * max(times)
    result = 0
    while first <= end:
        mid = (first + end) // 2
        count = 0
        for t in times:
            count += mid // t
            if count >= n :
                result = mid
                break
        if count >= n:
            end = mid - 1
        elif count < n:
            first = mid + 1
    return result


n, times = 6, [7, 10]
print(solution(n, times))
