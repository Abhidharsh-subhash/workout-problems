def majority(array):
    result={}
    for i in array:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    max_count=0
    max_num=None
    for num,count in result.items():
        if count>max_count:
            max_count=count
            max_num=num
    return max_num


arr=[2,2,1,1,1,2,2]
print(majority(arr))