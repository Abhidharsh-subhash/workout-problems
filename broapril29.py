def min(array):
    right=0
    left=0
    dif=0
    result=[]
    for i in array:
        right+=i
    for i in range(len(array)):
        left+=array[i]
        right-=array[i]
        avg_left=left/(i+1)
        if len(array)-(i+1) !=0:
            avg_right=right/(len(array)-(i+1))
        else:
            avg_right=right/1
        dif=avg_left-avg_right
        result.append(dif)
    min=0
    for i in range(1,len(result)):
        if result[i]<result[min]:
            min=i
    return (min+1)

arr=[1,8,9,3]
print(min(arr))