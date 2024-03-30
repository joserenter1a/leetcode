"""
Leetcode #1929. Concatenation of Array

Author: Jose Renteria
"""

from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [el for el in range(2 * n)]
    print(ans)
    for i, el in enumerate(range(n)):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans

print(getConcatenation([1,2,3,1]))
