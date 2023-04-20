def length(s):
    n=0
    a=0
    s+=' '
    for i in range(len(s)):
        if s[i]!=' ':
            n+=1
        else:
            if n>0:
                a=n
            n=0
    return a

print(length('a ab abh abhi'))