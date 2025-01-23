# Leetcode 35 Search Insert Position
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    
    low, high = 0, len(nums) 
    
    while low < high:
        mid = (high + low) >> 1
        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1
    return low # the low index is where the target WOULD be
    
if __name__ == '__main__':

    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target))
