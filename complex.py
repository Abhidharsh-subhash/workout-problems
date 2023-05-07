# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

#here the time complexity is O(n^2)
def check(array,k):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                s=abs(i-j)
                if s<=k:
                    return True
    return False

nums = [1,2,3,1,2,3]
k=2
# print(check(nums,k))

# time complexity with O(n)
def checks(array,k):
    seen={}
    for i,num in enumerate(array):
        # here i is the index and num is the value
        if num in seen and i-seen[num]<=k:
            return True
        seen[num]=i
    return False

nums = [1,0,1,1]
k=1
print(checks(nums,k))
