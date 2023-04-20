def intersection(array1,array2):
    result=[]
    for i in array1:
        if i in array2:
            if i not in result:
                result.append(i)
    return result

arr1=[4,9,5]
arr2=[9,4,9,8,4]
print(intersection(arr1,arr2))
