from typing import List

def plusOne(digits: List[int]) -> List[int]:
    digits = [str(i) for i in digits]
    s = ''.join(digits)
    a = int(s) + 1
    l = list(str(a))
    l = [int(i) for i in l]
    return l
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9, 9]))