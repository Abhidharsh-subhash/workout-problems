def revstring(string):
    result=''
    while i<len(string):
        if string[i] == ' ':
            print(0)
            result+=' '
        else:
            print(1)
            j=i
            k=i
            while string[j] != ' ':
                print(2)
                j+=1
            l=j-1
            for p in range(l,k-1,-1):
                print(3)
                result+=string[p]
        i=l+1
    return result
string='hello world'
print(revstring(string))