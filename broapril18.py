#second largest element in an array

def second(array):
    if len(array)>1:
        a=array[0]
        b=array[1]
        for i in range(2,len(array)):
            if array[i] > a:
                b=a
                a=array[i]
            elif array[i] > b:
                b=array[i]
        return b

arr=[44,6,88,43,78,67,99]
print(second(arr))
    