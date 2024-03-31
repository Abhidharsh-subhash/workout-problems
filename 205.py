from collections import Counter

def isIsomorphic(s: str, t: str):
        x=Counter(s)
        y=Counter(t)
        print(x, y)
        breakpoint()
        if len(x) == len(y):
            return True
        else:
            return False
    
s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s,t))