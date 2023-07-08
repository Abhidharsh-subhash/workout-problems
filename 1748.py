# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

def sumOfUnique(nums):
    result=0
    for i in nums:
        if nums.count(i) == 1:
            result+=i
    return result
nums = [1,2,3,4,5]
print(sumOfUnique(nums))
