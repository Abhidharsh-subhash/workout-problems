# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

def merge(nums1,m,nums2,n):
    if m == 0:
        return nums2
    elif n == 0:
        return nums1
    else:
        result=[]
        i=j=0
        while i<m and j<n:
            if nums1[i]>nums2[j]:
                result.append(nums2[j])
                j+=1
            else:
                result.append(nums1[i])
                i+=1
        while i<m:
            result.append(nums1[i])
            i+=1
        while j<n:
            result.append(nums2[j])
            j+=1
        return result
    
nums1 = [1,2,3,0,0,0]
m = 0
nums2 = [2,5,6]
n = 3
print(merge(nums1,m,nums2,n))


