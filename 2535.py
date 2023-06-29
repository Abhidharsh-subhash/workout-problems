# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.

def differenceOfSum(nums):
    sum=0
    dsum=0
    for i in nums:
        sum+=i
        for j in str(i):
            dsum+=int(j)
        
    return (sum-dsum)

nums = [1,2,3,4]
print(differenceOfSum(nums))
