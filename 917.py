# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

def reverseOnlyLetters(s):
    x=[i for i in s]
    start=0
    end=len(x)-1
    result=''
    while start<=end:
        if x[start].isalpha() and x[end].isalpha():
            x[start],x[end]=x[end],x[start]
            start+=1
            end-=1
        elif not x[start].isalpha():
            start+=1
        elif not x[end].isalpha():
            end-=1
    return result.join(x)

s="a-bC-dEf-ghIj"
print(reverseOnlyLetters(s))