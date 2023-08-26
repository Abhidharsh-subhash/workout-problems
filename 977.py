# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]
    return sorted(nums)

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))