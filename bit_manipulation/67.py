"""
LeetCode #67. Add binary

Author: Jose Renteria
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
