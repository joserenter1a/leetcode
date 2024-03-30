"""
LeetCode #136 Single Number

Author: Jose Renteria
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = 0
        for el in (nums):
            xorr = xorr ^ el
        return xorr
