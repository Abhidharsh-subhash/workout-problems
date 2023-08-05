# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

def pivotIndex(nums):    
    pivot=-1
    for i in range(len(nums)):
        left=0
        right=0
        if i == 0:
            right=sum(nums[i+1:])
            if left == right:
                pivot=i
                break
        elif i == len(nums)-1:
            left=sum(nums[:i])
            if left == right:
                pivot=i
                break
        else:
            left=sum(nums[:i])
            right=sum(nums[i+1:])
            if left == right:
                pivot=i
                break
    return pivot

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))