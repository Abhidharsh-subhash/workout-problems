# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.

def canBeIncreasing(nums):
    count=0
    i=0
    j=1
    while j<(len(nums)):
        if (nums[i]>nums[j]):
            count+=1
            nums.remove(nums[i])
        elif count>1:
            break
        else:
            i+=1
            j+=1
    if count == 1:
        return True,nums
    else: 
        return False,nums

nums = [2,3,1,2]
print(canBeIncreasing(nums))