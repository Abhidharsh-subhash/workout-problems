#input=[1,1,0,1,1,1] output=>3 most consecutive 1
#input=[1,0,1,1,0,1] output=>2

def consecutive(array):
    count=0
    for i in range(len(array)):
        if array[i] == 1:
            s=1
            for j in range(i+1,len(array)):
                if array[j] == 1:
                    s+=1
                else:
                    break
            if s>count:
                count=s
    return count

arr=[1,1,0,1,1,1]
print(consecutive(arr))

    