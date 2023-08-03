# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

def removeTrailingZeros(num):
    x=0
    for i in range(len(num)-1,-1,-1):
        if num[i] == '0':
            x+=1
        else:
            break
    return (num[:len(num)-x])
num = "51230100"
print(removeTrailingZeros(num))