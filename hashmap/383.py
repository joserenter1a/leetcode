"""

LeetCode #383.

Author: Jose Renteria

"""
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Initialize an empty hash map
    hash_map = {}
    # populate the hashmap with the {char:frequency}
    for el in magazine:
        if el in hash_map:
            hash_map[el] += 1
        else:
            hash_map[el] = 1

    # pointer
    head = 0
    # empty accumulator string
    emp = ""
    # go until I reach the end of the string
    while head <= len(ransomNote) - 1:
        # if the char is present in the hashmap and it's value is greater than 0
        if ransomNote[head] in hash_map and hash_map[ransomNote[head]] > 0:
            # accumulate that char to the empty string
            emp += ransomNote[head]
            # decrement the frequency in the hashmap for that char
            hash_map[ransomNote[head]] -= 1
        # move the pointer along no matter what
        head +=1
    # return the reconstructed string, if it is able to be constructed they will be equal
    return emp == ransomNote

sol = canConstruct("aa", "aab")
print(sol)