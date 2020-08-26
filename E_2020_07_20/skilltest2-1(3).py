from collections import deque
def solution(nums):
    s = deque(nums)
    a = deque("")
    for _ in range(len(nums)):
        if s == deque(""):
            break
        else:
            a += s.popleft()
            if a[-1] == s[0]:
                a.pop()
                s.popleft()
            else:
                s.append(a[-1])
                a.pop()
    if s == deque("") and a == deque(""):
        return 1
    else:
        return 0

if __name__ == "__main__":
    s = "baabaa"
    print(solution(s))