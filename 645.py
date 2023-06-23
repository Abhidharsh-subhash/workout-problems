# Input: nums = [1,2,2,4]
# Output: [2,3]

from collections import Counter


def findErrorNums(array):
    #it converts the array into dictionary of key value pairs
    c=Counter(array)
    result=[0,0]
    for i in range(len(nums)+1):
        if c[i] == 2:
            result[0]=i
        if c[i] == 0:
            result[1]=i
    return result

nums = [1,2,2,4]
print(findErrorNums(nums))
