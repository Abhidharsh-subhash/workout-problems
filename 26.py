# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeDuplicates(nums):
    result=set(nums)
    nums.clear()
    for i in result:
        nums.append(i)
    nums.sort()
    return len(nums)


nums = [1,1,2]
print(removeDuplicates(nums))