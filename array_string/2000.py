def reversePrefix(word: str, ch: str) -> str:
    if ch in word:
        bound = word.index(ch)  
    else :
        return word
    left_half = word[0:bound + 1]
    right_half = word[bound + 1:]
    emp = left_half[::-1] + right_half
    return emp

sol = reversePrefix('abcdefd', 'd')
print(sol)