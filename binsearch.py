# perform a binary search Leetcode 704
from typing import List 


def search(nums: List[int], target: int) -> int:
    high = len(nums) - 1
    low = 0
    while(low <= high):
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid +1
        elif nums[mid] > target:
            high = mid -1
        else:
            return mid
    return -1

if __name__ == '__main__':

    nums = [-1,0,3,5,9,12]
    target = 9
    print(search( nums, target))


    