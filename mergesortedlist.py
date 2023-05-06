#merge two sorted list with one is in ascending and other one is in descending order
def merge(array1,array2):
    result=[]
    l1=len(array1)
    i=0
    j=len(array2)-1

    while i<l1 and j>=0:
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j-=1
    while i<l1:
        result.append(array1[i])
        i+=1
    while j>=0:
        result.append(array2[j])
        j-=1
    return result

arr1=[1,3,5,7,9]
arr2=[8,6,4,2]
print(merge(arr1,arr2))