"""
LeetCode #242. Valid Anagram

Author: Jose Renteria
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
