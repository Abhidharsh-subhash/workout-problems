# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]

def createTargetArray(nums,index):
    result=[None]*len(nums)
    for i in range(len(nums)):
        x=index[i]
        y=nums[x]
        if result[x] is None:
            result[x]=y
        else:
            for j in range(i-1,-1,-1):
                print(result[j])
                result[j+1]=result[j]
            x=index[i]
            y=nums[x]
            result[x]=y
    print(result)

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums,index))