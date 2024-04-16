"""
LeetCode #80

Author: Jose Renteria
"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    cat, mouse = 1, 0
    curr_k = 0
    k = 0
    while cat != len(nums):
        if nums[cat] == nums[mouse]:
            
            curr_k += 1
        if curr_k >= 2:
            nums[cat], nums[mouse] = nums[mouse], nums[cat]
        cat += 1
        mouse += 1
    
    return nums

sol1 = removeDuplicates([1,1,1,2,2,3])
sol = removeDuplicates([0,0,1,1,1,1,2,3,3])
print(sol)
print(sol1)