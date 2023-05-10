# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def intersection(array1,array2):
    array1.sort()
    array2.sort()
    result=[]
    l1=len(array1)
    l2=len(array2)
    i=0
    j=0
    while i<l1 and j<l2:
        if array1[i] < array2[j]:
            i+=1
        elif array2[j] <  array1[i]:
            j+=1
        else:
            result.append(array1[i])
            i+=1
            j+=2
    return result

arr1=[4,9,5]
arr2=[9,4,9,8,4]
print(intersection(arr1,arr2))