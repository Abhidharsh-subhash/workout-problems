# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

def GCD(str1,str2):
    result=[]
    out=''
    for i in str1:
        if i in str2:
            result.append(i)
    res=set(result)
    for i in res:
        out+=i
    return out

str1 = "ABCABC"
str2 = "ABC"
print(GCD(str1,str2))
