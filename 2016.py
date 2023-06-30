# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

def maximumDifference(nums):
    result=0
    for i in range(1,len(nums)):
        for j in range(i,-1,-1):
            # print(nums[i],nums[j],nums[i]-nums[j])
            if nums[i]-nums[j]>result:
                result=nums[i]-nums[j]
    if result == 0:
        return -1
    else:
        return result
    
nums = [1,5,2,10]
print(maximumDifference(nums))