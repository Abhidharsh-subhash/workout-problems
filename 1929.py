# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

def getConcatenation(nums):
    result=nums * 2
    return result

nums = [1,2,1]
print(getConcatenation(nums))