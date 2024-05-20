"""

LeetCode #3. Longest Substring without Repeating Characters
Author: Jose Renteria
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    result = 0
    for r in s:
        while r in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(r)
        result = max(result, r - left + 1)
    return result