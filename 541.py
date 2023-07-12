# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

def reverseStr(s,k):
    result=''
    x=s[:k]
    result=result+x[::-1]
    result=result+s[k:]
    return result
return

s = "abcd"
k = 2
print(reverseStr(s,k))