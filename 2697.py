# Input: s = "egcfe"
# Output: "efcfe"
# Explanation: The minimum number of operations to make "egcfe" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "efcfe", by changing 'g'.

def makeSmallestPalindrome(s):
    x=[i for i in s]
    for i in range((len(x)//2)):
            if x[i] != x[len(x)-i-1]:
                a=min(x[i],x[len(x)-i-1])
                if x[i] == a:
                    x[len(x)-i-1] = a
                else:
                    x[i] = a
    return ''.join(x)
    

s = "seven"
print(makeSmallestPalindrome(s))
