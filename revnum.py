def reverse(x):
    value=x
    num=abs(x)
    revnum=0
    rem=0
    while num > 0:
        rem=num%10
        revnum=(revnum*10)+rem
        num=num//10
    if value>0:
        return revnum
    else:
        return -revnum
    
print(reverse(1534236469))
