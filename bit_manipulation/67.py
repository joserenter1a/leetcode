"""
LeetCode #67. Add binary

Author: Jose Renteria
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) 
        
        while low < high:
            mid = (high + low) >> 1
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low
