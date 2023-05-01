#input:nums=[3,0,1] output=>2
#input:nums=[0,1] output=>2

def missing(array):
    for i in range(len(array)+1):
        if i not in array:
            return i

arr=[1,2]
print(missing(arr))