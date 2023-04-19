def removeduplicates(array,target):
    k=[]
    for i in range(len(array)):
        if array[i] != target:
            k.append(array[i])
    return k

arr=[3,2,2,3]
print(removeduplicates(arr,3))
