def strStr(haystack,needle):
    l1=len(haystack)
    l2=len(needle)
    if (l1 and l2) > 0:
        index=haystack.find(needle)
        return index
    else:
        return -1   

print(strStr('amminiammayi','amma'))     