# Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# Output: 3
# Explanation:
# The strings in words which are a prefix of s = "abc" are:
# "a", "ab", and "abc".
# Thus the number of strings in words which are a prefix of s is 3.

def countPrefixes(words,s):
    result=0
    for i in words:
        n=len(i)
        if s[0:n] == i:
            result+=1
    return result
words=["e","s","mi","e","ia","ibwu","e","e","k","ci","rip","suw","a","l"]
s = "e"
print(countPrefixes(words,s))