# Leetcode 1800
# Max ascending subarray sum
from typing import List 

def maxAscendingSum( nums: List[int]) -> int:
    # start sum at head to accumulate to
    max_sum = nums[0]
    # store temp result in m
    m = 0
    for i in range(1, len(nums)):
        # if non ascending
        if nums[i] <= nums[i - 1]:
            # memoize results
            m = max(m, max_sum)
            # reset count
            max_sum = 0
        # accumulate
        max_sum += nums[i]
            
    return max(m, max_sum)