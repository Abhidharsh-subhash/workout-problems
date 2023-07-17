# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3

def twoOutOfThree(nums1,nums2,nums3):
    result=[]
    for i in nums1:
        if ((i in nums2) or (i in nums3)) and (i not in result):
            result.append(i)
    for i in nums2:
        if (i in nums3) and (i not in result):
            result.append(i)
    return result

nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(twoOutOfThree(nums1,nums2,nums3))