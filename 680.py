# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true

def validPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        delete=0
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                if delete < 1:
                    s[len(s)-i-1]=''
                    delete+=1
                else:
                    return False
        return True


s = "abca"
print(validPalindrome(s))
