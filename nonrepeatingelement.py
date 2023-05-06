#its time complexity is O(n^2)
def nonrepeating(array):
    for i in range(len(array)):
        count=0
        for j in range(len(array)):
            if i!=j and array[i] == array[j]:
                count+=1
                break
        if count == 0:
            return array[i]
    return None
        
arr=[4,1,2,1,2]
print(nonrepeating(arr))

#with time complexity O(n)
def nonrepeat(array):
    result={}
    for i in array:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    for i in result:
        if result[i] == 1:
            return i

print(nonrepeat(arr))
