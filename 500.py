def keyboard(array):
    t1='wertyuiop'
    t2='asdfghjkl'
    t3='zxcvbnm'
    result=[]
    for i in array:
        count1=0
        count2=0
        count3=0
        for j in i:
            if j.lower() in t1:
                count1+=1
            elif j.lower() in t2:
                count2+=1
            elif j.lower() in t3:
                count3+=1
            else:
                pass
        if count1==len(i) or count2==len(i)  or count3==len(i) :
            result.append(i)
    return result


string=["omk"]
print(keyboard(string))