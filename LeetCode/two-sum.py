from typing import List
def twoSum( nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, e in enumerate(nums):
        nums_map[e] = i
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            print(i, num)
            return nums.index(num), nums_map[target-num]
        
if __name__ == "__main__":
    nums, target = [3,3], 6
    print(twoSum(nums, target))