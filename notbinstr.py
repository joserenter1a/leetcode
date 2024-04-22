from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    sb = ""
    for i, el in enumerate(nums):
        if(el[i] == '1'):
            sb += '0'
        else: 
            sb += '1'
    return sb


findDifferentBinaryString(["01", "10"])