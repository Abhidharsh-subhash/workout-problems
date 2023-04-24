def find(array,target):
    a=0
    closest=float('inf')
    dif=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            sum=array[i]+array[j]
            dif=abs(target-sum)
            if closest > dif:
                closest=dif
                a=

arr=[4,8,2,10]
print(find(arr,9))
