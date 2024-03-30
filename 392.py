# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

def isSubsequence(s,t):
    # j=0
    # count=0
    # for i in s:
    #     while j<len(t):
    #         if t[j] == i:
    #             j+=1
    #             count+=1
    #             break
    #         elif t[j] != i:
    #             j+=1
    # if count == len(s):
    #     return True
    # else:
    #     return False
    x=y=0
    while x<len(s) and y<len(t):
        if s[x] != t[y]:
            y+=1
        else:
            x+=1
    if x == len(s):
        return True
    return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))