# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.

def maxProductDifference(nums):
    # x=max(nums)
    # m=nums.index(x)
    # y=min(nums)
    # n=nums.index(y)
    # a=b=float('inf')
    # j=k=0
    # for i in range(len(nums)):
    #     if i != m and x-nums[i] <= a:
    #         a=x-nums[i]
    #         j=nums[i]
    #     if i != n and (nums[i]-y >= 0 and nums[i]-y <= b):
    #         b=nums[i]-y
    #         k=nums[i]
    # print(x,a,j)
    # print(y,b,k)
    # return ((x*j) - (y*k))
    a=float('inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            x=nums[i]*nums[j]
            if x<a:
                a=x
    print(a)


nums = [2,9,5,9,1]
print(maxProductDifference(nums))