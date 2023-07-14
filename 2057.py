# Input: nums = [0,1,2]
# Output: 0
# Explanation: 
# i=0: 0 mod 10 = 0 == nums[0].
# i=1: 1 mod 10 = 1 == nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# All indices have i mod 10 == nums[i], so we return the smallest index 0.

def smallestEqual(nums):
    result=float('inf')
    for i in range(len(nums)):
        if i%10 == nums[i] and i<result:
            result=i
    if result != float('inf'):
        return result
    else:
        return -1


nums = [1,2,3,4,5,6,7,8,9,0]
print(smallestEqual(nums))