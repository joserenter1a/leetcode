"""
LeetCode #392. Is Subsequence

Author: Jose Renteria
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialize two pointers to the head of each str
        i, j = 0, 0
        # while they are both within bounds of their respective str's
        while i < len(s) and j < len(t):
            # if we find a match
            if s[i] == t[j]:
                # move the left pointer
                i += 1
            # the right pointer will be moved regardless
            j += 1        
        # if we are able to reach the end of the `s` then it is valid
        return True if i == len(s) else False
