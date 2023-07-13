# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.

def numOfStrings(patterns,words):
    result=0
    for i in patterns:
        if i in words:
            result+=1
    return result

patterns = ["a","b","c"]
word = "aaaaabbbbb"
print(numOfStrings(patterns,word))