from typing import List
def arrayPairSum(nums: List[int]) -> int:
    if len(nums) <= 2:
        return min(nums)
    nums.sort()
    nums_sum = 0
    for i in range(0,len(nums),2):
        nums_sum += nums[i]
    return nums_sum
if __name__ == "__main__":
    nums = [6,2,6,5,1,2]
    print(arrayPairSum(nums))
