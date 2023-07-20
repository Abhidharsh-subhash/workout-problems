# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrences(arr):
    # x=set(arr)
    # result=[]
    # for i in x:
    #     a=arr.count(i)
    #     if a not in result:
    #         result.append(a)
    #     else:
    #         return False
    # return True
    x={}
    for i in arr:
        if i not in x.keys():
            x[i]=1
        else:
            x[i]+=1
    a=len(x.values())
    b=len(set(x.values()))
    if a == b:
        return True
    else:
        return False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))