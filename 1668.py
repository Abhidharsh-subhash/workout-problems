# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

def arrayStringsAreEqual(arr1,arr2):
    result1=''
    result2=''
    for i in range(len(arr1)):
        result1+=arr1[i]
    for j in range(len(arr2)):
        result2+=arr2[j]
    if result1 == result2:
        return True
    else:
        return False

word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arrayStringsAreEqual(word1,word2))
