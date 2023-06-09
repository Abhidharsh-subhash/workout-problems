# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

def findNumbers(array):
    result=0
    for i in array:
        n=str(i)
        count=0
        for i in n:
            count+=1
        if count!=0 and count%2==0:
            result+=1
    return result

nums = [555,901,482,177]
print(findNumbers(nums))
