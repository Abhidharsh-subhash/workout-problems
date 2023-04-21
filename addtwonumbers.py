def add(array1,array2):
    result=[]
    s1,s2=0,0
    j1,j2=1,1
    for i in array1:
        s1=s1+(i*j1)
        j1=j1*10
    for i in array2:
        s2=s2+(i*j2)
        j2=j2*10
    r=s1+s2
    while r > 0:
        s=r%10
        result.append(s)
        r=r//10
    return result




arr1=[2,4,3]
arr2=[5,6,4]
print(add(arr1,arr2))
