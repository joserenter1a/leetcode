"""
Leetcode #66. Plus One

Author: Jose Renteria
"""
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits = [str(i) for i in digits]
    s = ''.join(digits)
    a = int(s) + 1
    l = list(str(a))
    l = [int(i) for i in l]
    return l

def plusOneAlt(digits: List[int]) -> List[int]:
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        if(len(digits) == 1):
            return [1, 0]
        else:
            return plusOne(digits[:-1]) + [0]
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9, 9]))
