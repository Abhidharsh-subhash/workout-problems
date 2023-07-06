# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

def minSubArrayLen(nums,target):
    left,right,total=0,0,0
    result=len(nums)+1
    while right<len(nums):
        total+=nums[right]
        right+=1
        while total >= target:
            result=min(result,right-left)
            total-=nums[left]
            left+=1
    if result == len(nums)+1:
        return 0
    else:
        return result
    
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(nums,target))