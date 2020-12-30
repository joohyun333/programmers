# https://www.acmicpc.net/problem/2938
import collections
N = int(input())
nums = collections.deque(map(int, input().split()))
result = []
stop_point = 0
# while len(nums)>1:
#     n = nums.popleft()
#     if (n+nums[0])%3!=0 or :
#         result.append(n)
#     elif (n+nums[0]) % 3 ==0:
#         stop_point+=1
#     else:
#         nums.append(n)
#     if stop_point == N-1:
#         print("-1")
#         break
print(result)
