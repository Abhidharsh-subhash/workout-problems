# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

def shuffle(nums,n):
    result=[]
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums,n))
