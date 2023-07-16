# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

def prefixCount(words,prefix):
    length=len(prefix)
    result=0
    for i in words:
        if i[:length] == prefix:
            result+=1
    return result
words = ["leetcode","win","loops","success"]
pref = "code"
print(prefixCount(words,pref))
