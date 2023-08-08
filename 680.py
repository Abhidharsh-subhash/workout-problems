# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true

def validPalindrome(s):
    x=[i for i in s] 
    delete=0
    i=0
    while i <= len(x)//2:
        if x[i]!=x[len(x)-i-1]:
            if delete < 1 and (x.count(x[len(x)-i-1]) == 1):
                x.pop(len(x)-i-1)
                delete+=1
                i=i
            elif delete < 1 and (x.count(x[i]) == 1):
                x.pop(i)
                delete+=1
                i=i
            else:
                return False
        i+=1
    return True

s = "tcaac"
print(validPalindrome(s))
