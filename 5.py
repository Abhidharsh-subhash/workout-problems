# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

def longestPalindrome(s):
    length=0
    result=''
    if len(s) == 1:
        result=s
    elif len(s) == 2 and s[0]!=s[1]:
        result=s[0]
    else:
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    x=s[i:j+1]
                    y=x[::-1]
                    if x == y and len(x) > length:
                        length=len(x)
                        result=x
        if len(result) == 0:
            result=s[0]
    return result

s="abcda"
print(longestPalindrome(s))