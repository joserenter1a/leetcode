"""
LeetCode #69. Sqrt(x)

Author: Jose Renteria
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  # base case
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                right = mid - 1
            else:
                left = mid + 1
