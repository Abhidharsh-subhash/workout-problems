# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveend(array):
    l=len(array)-1
    for i in range(l,-1,-1):
        if array[i] == 0:
            for j in range(i,l):
                array[j],array[j+1]=array[j+1],array[j]
            l-=1
    return array

arr=[0,0,1]
print(moveend(arr))
