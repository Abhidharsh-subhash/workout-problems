def minmax(array):
    min=array[0]
    max=0
    for i in array:
        if i > max:
            max=i
    for i in array:
        if i < min:
            min=i
    return max,min

print(minmax([2,5,8,90,6]))