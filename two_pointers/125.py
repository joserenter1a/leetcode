"""
Leetcode #125. Valid Palindrome

Author: Jose Renteria
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Intuition here is to check if it is the same string when it is reversed
    # helper function to determine if a value is alphanumerical
        def alpha_num(c):
            c = c.lower()
            # The same as decimal ranges [48, 57] and [97, 122]
            if (ord(c) >  47) and (ord(c) < 58):
                return True
            elif (ord(c) > 96) and (ord(c) < 123):
                return True
            else:
                return False
        # Accumulate a new string if it is alphanumerical, and compare against its reversed self
        newStr = ""
        for c in s:
            if alpha_num(c):
                newStr += c.lower()
        return newStr == newStr[::-1]
