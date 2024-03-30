def isSubsequence( s: str, t: str) -> bool:
    i = 0

    if len(t) == 0:
        return 0
    for char in t:
        if i >= (len(s) - 1):
            return True
        elif s[i] == char:
            i += 1
    return False

s = "abc"
t = "ahbgdc"
sol = isSubsequence(s, t)
print(sol)