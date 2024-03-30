# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    # s=s.lower()
    # string=''
    # for i in s:
    #     if i.isalpha() or i.isnumeric():
    #         string+=i
    # if string == string[::-1]:
    #     return True
    # return False
    s=s.lower()
    x=''
    for i in range(len(s)-1,-1,-1):
        if s[i].isalpha():
            x+=s[i]
    if x == x[::-1]:
        return True
    else:
        return False

s="0P"
print(isPalindrome(s))