#here space complexity is o(n) and time comlexity is O(n^2)
def unique(array):
    result=[]
    for i in array:
        if i not in result:
            result.append(i)
    return result


arr=[1,6,4,6,3,5,8,4,8]
print(unique(arr))

#here space complexity is O(n) and time complexity is O(n)
#wrong
def uniq(array):
    my_dict={}
    for i in array:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    for i,count in my_dict.items():
        if count == 1:
            print(i)

uniq(arr)