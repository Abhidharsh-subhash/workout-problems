# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

def findGCD(nums):
    x=min(nums)
    y=max(nums)
    if x == y:
        return x
    elif y%x == 0:
        return x
    result=1
    for i in range(1,x+1):
        if (x%i == 0) and (y%i == 0) and (result < i):
            result=i
    return result


nums = [3,3]
print(findGCD(nums))
