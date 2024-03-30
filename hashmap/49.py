"""
Leetcode #49. Group Anagrams

Author: Jose Renteria
"""

def groupAnagrams(strs):
    ana = {}
    for word in strs:
        sorted_word="".join(sorted(word))
        if sorted_word not in ana:
            ana[sorted_word]=[word]
        else:
            ana[sorted_word].append(word)
    return ana.values()
  

print(groupAnagrams([""]))
print(len([""]))
