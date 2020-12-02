# https://leetcode.com/problems/group-anagrams/submissions/
from typing import List
import collections
import re
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    strs_list = collections.defaultdict(list)
    for i in strs:
        strs_list[''.join(sorted(list(i)))].append(i)
    return list(strs_list.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))