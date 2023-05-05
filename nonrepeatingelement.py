#incomplete
def nonrepeating(array):
    count=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count+=1
        if count == 0:
            return array[i]
        
arr=[2,2,1]
print(nonrepeating(arr))
