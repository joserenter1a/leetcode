"""
Leetcode #269. Missing Number

Author: Jose Renteria
"""
def missingNumber(nums: List[int]) -> int:
    if len(nums) not in nums:
        return len(nums)
    for el in (range(len(nums))):
        if el not in nums:
            return el
        

print(missingNumber([3,0,1]))
print(missingNumber([0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

