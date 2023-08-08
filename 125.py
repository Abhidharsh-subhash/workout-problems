# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    s=s.lower()
    string=''
    for i in s:
        if i.isalpha() or i.isnumeric():
            string+=i
    if string == string[::-1]:
        return True
    return False

s="0P"
print(isPalindrome(s))