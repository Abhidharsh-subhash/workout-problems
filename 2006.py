# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

def countKDifference(nums,k):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i]-nums[j]) == k:
                count+=1
    return count
nums = [3,2,1,5,4]
k = 2
print(countKDifference(nums,k))
