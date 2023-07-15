# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

def intersection(nums):
    x={}
    result=[]
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            a=nums[i][j]
            if a not in x:
                x[a]=1
            else:
                x[a]+=1
    for i,j in x.items():
        if j == len(nums):
            result.append(i)
    print(x)
    print(result)
    y=sorted(result)
    print(y)
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(intersection(nums))