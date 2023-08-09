arr=[6,6,8,10,4,15,6,3,9,6]
#move all elements to the end of the array
def end(arr):
    n=len(arr)-1
    i=0
    while i<n:
        if arr[i] == 6:
            while i<n and arr[n] == 6:
                n-=1
            if n>i:
                arr[n],arr[i]=arr[i],arr[n]
        i+=1
    return arr

print(end(arr))

