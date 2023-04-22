def maximum(array):
    product=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            s=array[i]*array[j]
            if product < s:
                product = s
    return product

arr=[2,3,4,2,4]
print(maximum(arr))