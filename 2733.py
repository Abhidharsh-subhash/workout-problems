# Input: nums = [3,2,1,4]
# Output: 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.

def findNonMinOrMax(array):
    high=max(array)
    low=min(array)
    for i in array:
        if i!=high and i!=low:
            return i
    return -1

nums = [3,2,1,4]
print(findNonMinOrMax(nums))