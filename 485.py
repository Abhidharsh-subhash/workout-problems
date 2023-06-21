# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

def findMaxConsecutiveOnes(array):
    result=0
    count=0
    array.append(0)
    for i in array:
        if i:
            count+=1
        else:
            result = max(count,result)
            count=0
    return result

nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))