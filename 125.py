def isPalindrome( s: str) -> bool:

    # helper function to determine if a value is alphanumerical
    def alpha_num(c):
        c = c.lower()
        # The same as decimal ranges [48, 57] and [97, 122]
        if (ord(c) >  47) and (ord(c) < 58):
            return True
        elif (ord(c) > 96) and (ord(c) < 123):
            return True
        else:
            return False
    newStr = ""
    for c in s:
        if alpha_num(c):
            newStr += c.lower()
    return newStr == newStr[::-1]


sol = isPalindrome("amanaplanacanalpanama")
print(sol)