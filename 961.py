# You are given an integer array nums with the following properties:

# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

 

# Example 1:

# Input: nums = [1,2,3,3]
# Output: 3

def repeatedNTimes(nums):
    n=len(nums)//2
    for i in nums:
        if nums.count(i) == n:
            return i

nums = [5,1,5,2,5,3,5,4]
print(repeatedNTimes(nums))