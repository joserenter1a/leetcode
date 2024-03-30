"""
LeetCode #9. Palindrome Number

Author: Jose Renteria
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        rev = temp[::-1]
        return temp == rev
