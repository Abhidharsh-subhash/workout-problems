# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

def removeTrailingZeros(num):
    array=[x for x in num]
    print(array)
    for i in array:

num = "51230100"
print(removeTrailingZeros(num))