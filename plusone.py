def plusone(array):
    count=0
    j=0
    for i in range(1,len(array)+1):
        j=j*10
        if j==0:
            j=1
        count=count+array[len(array)-i]*j
    count=count+1

    result=[int(x) for x in str(count)]
    return result

arr=[9,9]
print(plusone(arr))

