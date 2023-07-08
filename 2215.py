# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

def findDifference(nums1,nums2):
    x=[]
    x1=[]
    x2=[]
    for i in nums1:
        if i not in nums2 and i not in x1:
            x1.append(i)
    for i in nums2:
        if i not in nums1 and i not in x2:
            x2.append(i)
    x.append(x1)
    x.append(x2)
    return x
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1,nums2))