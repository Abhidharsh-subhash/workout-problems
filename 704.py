# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
def search(array,target):
    left = 0
    right = len(array)-1
        
    while left<=right:
        mid = (left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return -1

nums = [-1,0,3,5,9,12]
target =9
print(search(nums,target))