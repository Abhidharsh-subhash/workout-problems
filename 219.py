# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def containsNearbyDuplicate(nums,k):
    # result=False
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] == nums[j]:
    #             if abs(i-j)<=k:
    #                 result=True
    #                 break
    #     if result == True:
    #         break
    # return result
    x={}
    for i in range(len(nums)):
        if nums[i] not in x.keys():
            x[nums[i]]=[i]
        else:
            y=x[nums[i]]
            for j in range(len(y)):
                
                if abs(i-j)<=k:
                    return True
            x[nums[i]].append(i)
    return False

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums,k))
