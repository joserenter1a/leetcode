"""
LeetCode #1768. Merge Strings Alternatively

Author: Jose Renteria
"""
def mergeAlternately(w1: str, w2: str) -> str:
    first = 0
    emp = ""
    for i in range(max(len(w1), len(w2))):
        if i < len(w1):
            emp += w1[i]
        if i < len(w2):
            emp += w2[i]
    return emp

sol = mergeAlternately("abc", "pqrs")
print(sol)