# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeDuplicates(nums):
    x=[]
    i=0
    while i<len(nums):
        if nums[i] not in x:
            if i == len(nums)-1:
                x+=[nums[i]]
            elif nums[i] == nums[i+1]:
                x+=[nums[i],nums[i+1]]
                i+=2
            elif nums[i] != nums[i+1]:
                x+=[nums[i]]
                i+=1
        else:
            i+=1
    nums[:]=x
    return len(nums)
nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))