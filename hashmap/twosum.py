from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {} # {val: index}
    for i, el in enumerate(nums):
        diff = target - el
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[el] = i
    return

sol = twoSum([2,7,11,15], 9)

print(sol)