def numberOfSpecialChars( word: str) -> int:
    lowers = set()
    uppers = set()

    ct = 0
    for char in word:
        if ord(char) < 97:
            uppers.add(char)
        else:
            lowers.add(char)
    print(lowers)
    print(uppers)
    for char in word:

        if char in uppers and (char.lower() in lowers) or char in lowers and (char.upper() in uppers):
            print(char, ct)
            uppers.remove(char.upper())
            lowers.remove(char.lower())
            ct += 1
    return ct

sol = numberOfSpecialChars("aaAbcBC")
print(sol)