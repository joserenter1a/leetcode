# LeetCode 1455 Check if a word occurs as a prefix of any word in a sentence
# Example
# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

def isPrefix(sentence: str, searchWord: str) -> int:
    sentence = sentence.split()
    f = len(searchWord)
    for i, word in enumerate(sentence):
        print(word[i:f])
        if searchWord in word and word[0:f] == searchWord:
        
            return i + 1
    return -1


if __name__ == "__main__":
    ans = isPrefix("i love eating burger",  "burg")
    print(ans)