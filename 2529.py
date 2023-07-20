# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

def maximumCount(nums):
    pos=0
    neg=0
    for i in nums:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
    return max(pos,neg)
    
nums = [-2,-1,-1,1,2,3]
print(maximumCount(nums))