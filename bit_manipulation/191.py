"""
LeetCode #191. Number of 1 Bits

Author: Jose Renteria
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans
