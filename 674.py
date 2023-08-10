# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.

def findLengthOfLCIS(nums):
    result=1
    i=0
    while i<len(nums)-1:
        count=1
        if nums[i] < nums[i+1]:
            count+=1
            j=i+1
            while j < len(nums)-1:
                if nums[j] < nums[j+1]:
                    count+=1
                    j+=1
                else:
                    i=j
                    break
            if count > result:
                result=count
        i+=1
    return result

nums = [1,3,5,4,7]
print(findLengthOfLCIS(nums))
