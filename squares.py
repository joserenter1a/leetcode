# Leetcode 977 Squares of Sorted Array

def sortedSquares(nums: list[int]) -> list[int]:
    result = []
    low, high = 0, len(nums) - 1

    while low <= high:
        if abs(nums[low]) > abs(nums[high]):
            result.append(nums[low] ** 2)
            low += 1
        else:
            result.append(nums[high] ** 2)
            high -= 1
        
    return result[:: -1]

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    out = [16,1,0,9,100]
    print(sortedSquares(nums))