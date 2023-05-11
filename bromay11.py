#incomplete
def number(str):
    s=0
    for i in str:
        if i == ' ':
            s+=1
    return s

s='hello, my name is john'
print(number(s))