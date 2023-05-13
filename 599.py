def minindex(array1,array2):
    result=[]
    k=float('inf')
    for i in range(len(array1)):
        for j in range(len(array2)):
            s=0
            if array1[i] == array2[j]:
                s=i+j
                if k>s:
                    k=s
                    if len(result)!=0:
                        result.pop()
                    result.append(array1[i])
                if k==s and (array1[i] not in result):
                    result.append(array1[i])
    return result

arr1=["happy","sad","good"]
arr2=["sad","happy","good"]
print(minindex(arr1,arr2))
