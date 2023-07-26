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
    result=[]
    for n,i in zip(nums,index):
        result.insert(i,n)
    return result

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums,index))