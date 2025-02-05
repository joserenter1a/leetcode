# LeetCode 1790

def areAlmostEqual(s1: str, s2: str) -> bool:
    # strings must contain same amount & set of chars
    if sorted(s1) != sorted(s2):
        return False
    # base case
    if s1 == s2:
        return True
    # keep count of differences
    ct = 0
    # iterate over string compare diffs
    for i, el in enumerate(s1):
        if el != s2[i]:
            ct += 1
    return True if ct <= 2 else False