def sum(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return i,j
    return 'not found'

arr=[1,6,9,2,5]
print(sum(arr,8))