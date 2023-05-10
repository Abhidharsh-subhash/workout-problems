#input=>[1,2,3] output=>[1,2,4]

def add(array):
    s=0
    r=1
    result=[]
    for i in range(len(array)-1,-1,-1):
        s+=array[i]*r
        r=r*10
    res=s+1
    for i in str(res):
        result.append(int(i))
    return result

print(add([1,1,9]))
