def missing(array):
    n=len(array)+1
    total=(n*(n+1))/2
    s=0
    for i in array:
        s+=i
    return int(total-s)

arr=[1,2,3,5]
print(missing(arr))