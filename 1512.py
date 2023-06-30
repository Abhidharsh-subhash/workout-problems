# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

def numIdenticalPairs(nums):
    result=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                result+=1
    return result

nums = [1,1,1,1]
print(numIdenticalPairs(nums))