# Leetcode 3105 Longest Strictly Increasing or Strictly Decreasing Subarray
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc_length = 1
        dec_length = 1
        maxlength = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_length += 1
                dec_length = 1

            elif nums[i] < nums[i - 1]:
                dec_length += 1
                inc_length = 1

            else:
                inc_length = 1
                dec_length = 1
            maxlength = max(maxlength, max(inc_length, dec_length))
        return maxlength