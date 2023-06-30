# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):
    result=[]
    for i in range(len(nums)):
        sum=0
        for j in range(i,-1,-1):
            sum+=nums[j]
        result.append(sum)
    return result

nums = [1,2,3,4]
print(runningSum(nums))
        
