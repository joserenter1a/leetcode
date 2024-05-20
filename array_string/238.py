"""
Leetcode #238. Product of Array Except Self

Author: Jose Renteria


"""

from typing import List 

def productExceptSelf(nums: List[int]) -> List[int]:
    def find_list_wo(i: int):
        if i == 0:
            return nums[1:]
        else:
            list_wo_right = nums[i + 1:]
            list_wo_left = nums[0: i]
            list_wo = list_wo_left + list_wo_right
        return list_wo
    sums = []
    from functools import reduce  # Required in Python 3
    import operator
    def prod(iterable):
        return reduce(operator.mul, iterable, 1)
    
    for i, el in enumerate(nums):
        l_to_calc = find_list_wo(i)
        print(l_to_calc)
        s = prod(l_to_calc)
        sums.append(s)
    return sums

nums = [1,2,3,4]
Output = [24,12,8,6]
sol = productExceptSelf(nums)
print(sol)