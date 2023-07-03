# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

def countConsistentStrings(allowed,words):
    allowed=set(allowed)
    count=0
    for i in words:
        for j in i:
            if j not in allowed:
                count+=1
                break
    return (len(words)-count)

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed,words))
