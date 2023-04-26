#input=>[1,2,5,8] input=>6 output=>[1,2,5,6,8]
#incomplete
def insert(array,value):
    l=len(array)
    # i=l-1
    # while i>=0 and array[i]>value:
    #     array[i+1]=array[i]
    #     i-=1
    # array[i+1]=value
    # return array 
    for i in range(l):
        if array[i]<value and array[i+1]>value:
            array.insert(i+1,value)
    return array

arr=[1,2,5,8]
print(insert(arr,3))