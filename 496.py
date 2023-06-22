# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

def nextGreaterElement(array1,array2):
    result=[]
    for i in array1:
        for j in range(len(array2)):
            flag=1
            val=0
            if i==array2[j]:
                val=array2[j]
                for k in range(j+1,len(array2)):
                    if array2[k]>val:
                        result.append(array2[k])
                        flag=0
                        break
                if flag == 1:
                    result.append(-1)
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))