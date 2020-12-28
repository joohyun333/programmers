# https://leetcode.com/problems/assign-cookies/
from typing import List
import bisect
def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    result = 0
    for i in s:
        index = bisect.bisect_right(g,i)
        print(index)
        if index > result:result+=1
    return 0
if __name__ == "__main__":
    g = [1,2]
    s = [1,2,3]
    print(findContentChildren(g, s))