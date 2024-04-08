# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a,b): 
    if len(a)>len(b):
        for i in range(len(a)-len(b)):
            b='0'+b
    elif len(b)>len(a):
        for i in range(len(b)-len(a)):
            a='0'+a
    rem=0
    result=''
    for i in range(len(a)-1,-1,-1):
        if (a[i]=='0' and b[i]=='1') or (a[i]=='1' and b[i]=='0'):
            if rem == 0:
                result='1'+result
            elif rem==1 and i==0:
                result='10'+result
            elif rem == 1:
                result='0'+result
                rem=1
        elif a[i]=='0' and b[i]=='0':
            if rem == 0:
                result='0'+result
            else:
                result='1'+result
                rem=0
        elif a[i]=='1' and b[i]=='1':
            if rem==0 and i==0:
                result='10'+result
            elif rem==1 and i==0:
                result='11'+result
            elif rem==0:
                result='0'+result
                rem=1
            elif rem==1:
                result='1'+result
                rem=1
    return result

        
a = "1010"
b = "1011"
print(addBinary(a,b))