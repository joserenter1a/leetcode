from collections import deque as stack
def removeStars( s: str) -> str:
    st = stack()
    for char in s:
        if char == '*':
            st.pop()
        else:
            st.append(char)
    s = ""
    for c in st:
        s += (c)
    return s

sol = removeStars("leet**cod*e")
print(sol)