"""
LeetCode #128 

Author: Jose Renteria

"""

# 1. Handling edge cases:
    # - if len(nums) == 0 or len(nums) == 1, the length is the longest consecutive sequence,
    # So return the len(nums)
# 2. Initializing Data Structures:
    # - Hashmap to store the unique elements from the nums array
    # count = 1, tracks the length of the current consecutive sequence
    # ans = 1, tracks the longest sequence found so far
# 3. Adding elements to the hashmap
    # - for loop iterating through each element in the nums array
    # add nums[i], add the current element to the hashmap, checks for existence of consecutive elements later
# 4. Iterating through hashmap and checking sequence
    # outer for loop iterates through each element in the hashmap
        # Skip existing sequences, if (hashmap contains (it - 1) continue)
        # This condition checks that the previous elmeent exists in the hashmap
        # If true, it means the element (it) has been processed and is part of an existing sequence
        # the continue statement skips to the next element in the hashmap to avoid redundant processing
    # Finding a new sequence start
        # next_val = it + 1; if the previous element wasn't found, it potentially
        # marks the beginning of a new sequence. next_val stores the value
        # expected for the next element in the sequence
        # if the hashmap contains(next_val), confirms the start of a consecutive sequence
# 5. Calculating sequence length
    # Inner loop and count update:
        # The inner while loop iterates as long as elements with increasing values (next_val) exist
        # count += 1: increment count for each el in sequence
        # next_val += 1; increment next_val to check for the next element in the potential sequence
    # Updating longest sequence
        # ans = Math.max(ans, count): after the inner loop, the current count represents the length of the sequence starting at (it)
        # Max compares it to the previous answer and updates it accordingly.
# 6. Resetting count for non-sequences:
        # else count = 1; if next_val wasn't found in the hashmap, it signifies that (it) is not part of a sequence
        # reset the count to 1 for the next iteration in the outer loop
# 7. Returning the result
    # after iterating through all elements in the hashmap, the ans variable holds the length of the longest consecutive sequence found, return ans
    

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    # edge case checking
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    
    hash_set = set(el for el in nums)
    print(hash_set)
    count = 1
    ans = 1
    for it in hash_set:
        if (it - 1) in hash_set:
            continue
        next_val = it + 1
        while (next_val) in hash_set:
            count += 1
            next_val += 1
            ans = max(ans, count)
        else:
            count = 1
    return ans
    
nums = [0,3,7,2,5,8,4,6,0,1]

negative_nums = [9,1,4,7,3,-1,0,5,8,-1,6]


# Expected 9
sol = longestConsecutive(nums)

# Expected 7
sol_neg = longestConsecutive(negative_nums)

print(sol)
print(sol_neg)