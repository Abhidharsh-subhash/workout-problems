#BASEBALL GAME

def baseball(scores):
    result=[]
    for i in scores:
        if i == "C":
            result.pop()
        elif i == "D":
            x=int(result[-1]) * 2
            result.append(str(x))
        elif i == "+":
            a=int(result[-1]) + int(result[-2])
            result.append(str(a))
        else:
            result.append(i)
        
    s=0
    if len(result) == 0:
        return 0
    else:
        for i in result:
            s+=int(i)
        return s
    
ops = ["1","C"]
print(baseball(ops))