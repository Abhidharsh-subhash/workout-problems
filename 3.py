# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    result=''
    for i in range(len(s)):
        x=''
        x+=s[i]
        for j in range(i+1,len(s)):
            if s[j] not in x:
                x+=s[j]
            else:
                break
        if len(x) > len(result):
            result=x
    return len(result)


s = "pwwkew"
print(lengthOfLongestSubstring(s))
