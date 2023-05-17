def romantoint(s):
    sum=0
    translations={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    s=s.replace('IV','IIII').replace('IX','VIIII')
    s=s.replace('XL','XXXX').replace('XC','LXXXX')
    s=s.replace('CD','CCCC').replace('CM','DCCCC')
    for i in s:
        sum+=translations[i]
    return sum

s = "MCMXCIV"
print(romantoint(s))
