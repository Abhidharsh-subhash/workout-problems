# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(arr,target):
    x=[]
    x.append(arr[0])
    result=[]
    for i in range(1,len(arr)):
        if (target - arr[i]) in x:
            result.append(arr.index(target - arr[i]))
            result.append(i)
        else:
            x.append(arr[i])
    return result

nums = [3,2,4]
target = 6
print(twoSum(nums,target))