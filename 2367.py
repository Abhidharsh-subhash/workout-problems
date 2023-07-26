# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 

def arithmeticTriplets(nums,diff):
    result=0
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         for k in range(j+1,len(nums)):
    #             if (i<j and j<k) and ((nums[j]-nums[i] == diff) and (nums[k]-nums[j] == diff)):
    #                 result+=1
    # return result
    n = len(nums)
    for i in range(n):
        if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
            result += 1
        
    return result
nums = [4,5,6,7,8,9]
diff = 2
print(arithmeticTriplets(nums,diff))
