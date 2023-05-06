#its time complexity is O(N)
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
