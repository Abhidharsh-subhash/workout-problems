def common(array1,array2):
    result=[]
    for i in array1:
        if i in array2:
            result.append(i)
    return result

arr1=[]
arr2=[]
n1=int(input('number of elements in first array '))
for i in range(n1):
    el=int(input())
    arr1.append(el)
n2=int(input('number of elements in second array '))
for i in range(n2):
    el=int(input())
    arr2.append(el)
print(common(arr1,arr2))