#input=[12,4,8,3],output=>[5,-5,-17,-24]
#12=(4+8+3)-0,4=(8+3)-12,8=3-(12+4),3=0-(12+4+8) is the output
def new(array):
    result=[]
    for i in range(len(array)):
        if i==0:
            j=i+1
            s=0
            while j<len(array):
                s+=array[j]
                j+=1
            result.append(s)
        else:
            j=i+1
            k=i-1
            p=0
            q=0
            s=0
            while j<len(array):
                p+=array[j]
                j+=1
            while k>=0:
                q+=array[k]
                k-=1
            s=p-q
            result.append(s)
    return result
print(new([12,8,4,3]))