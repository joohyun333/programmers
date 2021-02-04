import sys
import collections
input = sys.stdin.readline
for i in range(int(input())):
    N, M = map(int, input().split())
    s = collections.deque(map(int, input().split()))
    s_ = collections.deque([False]*N)
    s_[M] = True
    count = 0
    while s:
        s_max = max(s)
        first, s_first = s.popleft(), s_.popleft()
        if s_max == first:
            if s_first:
                count+=1
                print(count)
                break
            else:
                count += 1
        else:
            s.append(first)
            s_.append(s_first)