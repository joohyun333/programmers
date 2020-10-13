from typing import List
# def twoSum(nums:List[int], target:int) -> List[int]:
#     for i, n in enumerate(nums):
#         complement = target - n
#         if complement in nums[i+1:]:
#             print(complement,i)
#             return nums.index(n),nums[i+1:].index(complement) + (i+1)
def twoSum(nums:List[int], target:int) -> List[int]:
    nums_map = {}
    for i, e in enumerate(nums):
        nums_map[e] = i
    print(nums_map)
    for i, e in enumerate(nums):
        if target-e in nums_map and i != nums_map[target-e]:
            print(target-e, i)
            return nums.index(e), nums_map[target-e]

if __name__ == "__main__":
    nums = [15,7,11,2]
    target = 9
    print(twoSum(nums,target))