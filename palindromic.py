from typing import List
def groupPalindrome(strs: List[str]) -> List[List[str]]:
    pals = []
    def is_pal(el):
        return el == el[::-1]
    
    for el in strs:
        if is_pal(el):
            pals.append(el)
    return pals

inp = ["eat","tea","tan","ate","nat","bat", "ata"]
groupPalindrome(inp)

def missingNumber(nums: List[int]) -> int:
    if len(nums) not in nums:
        return len(nums)
    for el in (range(len(nums))):
        if el not in nums:
            return el
        

print(missingNumber([3,0,1]))
print(missingNumber([0, 1]))
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

def groupAnagrams(strs):
    anagrams = []
    if len(strs) == 1:
        return [strs]
    

print(groupAnagrams([""]))
print(len([""]))