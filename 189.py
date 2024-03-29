# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def rotate(nums,k):
    if k>0:
        result=[]
        for i in range(len(nums)-1,len(nums)-k-1,-1):
            result.append(nums[i])
            nums.remove(nums[i])
        result[:] = reversed(result)
        nums[:] = result+nums
        return nums

nums = [-1]
k = 2
print(rotate(nums,k))