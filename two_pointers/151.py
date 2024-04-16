"""
LeetCode #151. Reverse Words in a String

Author: Jose Renteria

"""

# The sky is blue ---> blue is sky the
# Use two pointer approach, must quantify start and end of a word.

def reverseWords(s: str):
    # Turn the str into a list
    s = s.split()
    # init empty str
    emp = " "
    # init your left and right pointers
    left, right = 0, len(s) - 1
    # While the left is less than the right ptr
    while left < right:
        # swap the two positions in the string at each pointer
        # so [sky, blue] turns into [blue, sky]
        s[left], s[right] = s[right], s[left]
        # Move the left pointer up one and the right pointer down one, it will decompose until they reach each other
        left += 1
        right -= 1
    # Accumulate the new string into an empty string from the new list we've swapped
    for word in s:
        emp += f'{word.strip()} '
    return emp.strip()

sol = reverseWords("sky blue is the")
print(sol)


from typing import List 

def alt_reverseWords(s: str) -> str:
    
    def str_to_list(string, delimiters=' \t\n'):
        result = []
        word = ''
        for c in string:
            if c not in delimiters:
                word += c
            elif word:
                result.append(word)
                word = ''
        if word:
            result.append(word)

        return result
        
    
    l = str_to_list(s)
    print(l)
    head, tail = 0, len(l) - 1

    while head < tail:
        l[head], l[tail] = l[tail], l[head]
        head += 1
        tail -= 1

    emp = ""
    for word in l:
        emp += f'{word.strip()} '

    return emp.strip()

sol = alt_reverseWords("a good   example")
print(sol)