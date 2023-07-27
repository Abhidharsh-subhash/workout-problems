# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverseString(s):
    print(s)
    n=len(s)-1
    print(n)
    if n%2 == 0:
        i=0
        while i<(n/2):
            print(i)
            s[i],s[n-i]=s[n-i],s[i]
            i+=1
    else:
        i=0
        while i<=(n/2):
            print(i)
            s[i],s[n-i]=s[n-i],s[i]
            i+=1
    print(s)
s=["h","e","l","l"]
print(reverseString(s))