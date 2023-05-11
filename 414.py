def thirdlargest(arrays):
    arr=set(arrays)
    array=list(arr)
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            return array[1]
    else:
        array.sort()
        return array[-3]
    
print(thirdlargest([2,2,3,1]))