def unique(array):
    count=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count+=1
    if count == 0:
        return True
    else:
        return False

arr=[1,2,3,4,5,6,7,8,8]
print(unique(arr))