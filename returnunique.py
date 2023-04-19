#here space complexity is o(n) and time comlexity is O(n^2)
def unique(array):
    result=[]
    for i in array:
        if i not in result:
            result.append(i)
    return result


arr=[1,6,4,6,3,5,8,4,8]
print(unique(arr))

def uniq(array):
    dictionary={}
    for i in array:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    for i,count in dictionary.items():
        if count == 1:
            print(i)

uniq(arr)