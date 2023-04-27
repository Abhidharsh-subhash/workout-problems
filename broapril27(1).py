def new(array):
    left=0
    right=0
    result=[]
    for i in array:
        right+=i
    for i in range(len(array)):
        right-=(left+array[i])
        result.append(right)
        left+=array[i]
    return result

arr=[12,8,4,3]
print(new(arr))