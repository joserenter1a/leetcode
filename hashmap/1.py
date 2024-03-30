"""
LeetCode #1. Two Sum

Author: Jose Renteria
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize empty hashmap
        hash_map = {}
        
        #get the index and value n from nums using enumerate
        for i, n in enumerate(nums):
            diff = target - n # getting the difference between target value and n
            # Check if difference is in Hashmap or not
            if diff in hash_map:
                return [hash_map[diff], i] #if present return index of both values
            hash_map[n] = i #if not update the hashmap
        return
