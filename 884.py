# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

def uncommonFromSentences(s1,s2):
    result=[]
    x=s1.split(' ')
    y=s2.split(' ')
    for i in x:
        if (i not in y) and (x.count(i) == 1):
            result.append(i)
    for i in y:
        if (i not in x) and (y.count(i)  == 1):
            result.append(i)
    return result
    

s1 = "apple apple"
s2 = "banana"
print(uncommonFromSentences(s1,s2))