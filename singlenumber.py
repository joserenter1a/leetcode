from typing import List

def singleNumberHash(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    count = {}
    
    for i, el in enumerate(nums):
        if el in count:
            count[el] += 1
        else:
            count[el] = 1
    fin = []
    for el in count:
        if count[el]  < 2:
            fin.append(el)

    return(fin[0])

def singleNumberXOR(nums: List[int]) -> int:
    xorr = 0
    for el in (nums):
        xorr = xorr ^ el
    return xorr

singleNumberHash([4,2,1,2,1])

singleNumberXOR([1,2,1,2,4])