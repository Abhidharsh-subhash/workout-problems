def merge(array1,array2):
    l1=len(array1)
    l2=len(array2)
    i=0
    j=0
    result=[]
    while i<l1 and j<l2:
        if (array1[i]<array2[j]) and (array1[i]>0 and array2[j]>0):
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1
    while i<l1 and array1[i]>0:
        result.append(array1[i])
        i+=1
    while j<l2 and array2[j]>0:
        result.append(array2[j])
        j+=1
    return result


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,nums2))